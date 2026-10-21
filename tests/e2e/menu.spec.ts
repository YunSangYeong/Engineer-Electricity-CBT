import { expect, test, type Page } from '@playwright/test';

async function open(page: Page) {
  await page.getByRole('button', {name:'메뉴 열기'}).click();
  await expect(page.locator('.sidebar')).toHaveClass(/open/);
  // Transition must finish before picking input coordinates.
  await page.waitForTimeout(300);
}
async function visibleInViewport(page: Page, selector: string) {
  return page.locator(selector).evaluate(el=>{
    const rect=el.getBoundingClientRect();
    return rect.top>=0 && rect.bottom<=window.innerHeight;
  });
}
for(const viewport of [{width:390,height:480},{width:740,height:360}]) {
  test(`메뉴 실제 휠 상하 이동 ${viewport.width}×${viewport.height}`, async({page})=>{
    await page.setViewportSize(viewport); await page.goto(''); await open(page);
    const sidebar=page.locator('.sidebar');
    expect(await sidebar.evaluate(el=>el.scrollHeight>el.clientHeight)).toBe(true);
    const background=await page.evaluate(()=>scrollY);
    await page.mouse.move(120,180); await page.mouse.wheel(0,1400);
    await expect.poll(()=>visibleInViewport(page,'.sidebar-bottom button:last-of-type')).toBe(true);
    expect(await sidebar.evaluate(el=>el.scrollTop)).toBeGreaterThan(0);
    expect(await page.evaluate(()=>scrollY)).toBe(background);
    const download=page.waitForEvent('download');
    await page.getByRole('button',{name:'학습 기록 백업',exact:true}).click();
    expect((await download).suggestedFilename()).toContain('backup');
    await page.mouse.move(120,180); await page.mouse.wheel(0,-1400);
    await expect.poll(()=>sidebar.evaluate(el=>el.scrollTop)).toBe(0);
    await expect(page.getByRole('navigation').getByRole('button',{name:'학습 대시보드',exact:true})).toBeInViewport();
    await page.getByRole('navigation').getByRole('button',{name:'학습 대시보드',exact:true}).click();
    await expect(sidebar).not.toHaveClass(/open/);
    expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBe(true);
  });
}

test('모바일 터치 스와이프와 글자 확대·뷰포트 변경', async({page,context,browserName})=>{
  test.skip(browserName!=='chromium','CDP touch input requires Chromium');
  await page.setViewportSize({width:390,height:480});
  await page.goto('');
  // A separate CDP touch path; wheel is not used in this test.
  const cdp=await context.newCDPSession(page);
  await cdp.send('Emulation.setTouchEmulationEnabled',{enabled:true,maxTouchPoints:1});
  await open(page);
  const sidebar=page.locator('.sidebar');
  async function swipe(from:number,to:number) {
    await cdp.send('Input.dispatchTouchEvent',{type:'touchStart',touchPoints:[{x:120,y:from}]});
    for(let i=1;i<=12;i++) {
      await cdp.send('Input.dispatchTouchEvent',{type:'touchMove',touchPoints:[{x:120,y:from+(to-from)*i/12}]});
      await page.waitForTimeout(20);
    }
    await cdp.send('Input.dispatchTouchEvent',{type:'touchEnd',touchPoints:[]});
    await page.waitForTimeout(250);
  }
  for(let i=0;i<3;i++) await swipe(380,100);
  await expect.poll(()=>visibleInViewport(page,'.sidebar-bottom button:last-of-type')).toBe(true);
  expect(await sidebar.evaluate(el=>el.scrollTop)).toBeGreaterThan(0);
  const reset = await page.getByRole('button',{name:'데이터 초기화',exact:true}).boundingBox();
  if (!reset) throw new Error('Reset must be visible after touch scroll');
  await cdp.send('Input.dispatchTouchEvent',{type:'touchStart',touchPoints:[{x:reset.x+reset.width/2,y:reset.y+reset.height/2}]});
  await cdp.send('Input.dispatchTouchEvent',{type:'touchEnd',touchPoints:[]});
  await expect(page.getByRole('dialog')).toBeVisible();
  await page.getByRole('button',{name:'돌아가기',exact:true}).click();
  for(let i=0;i<3;i++) await swipe(100,380);
  await expect.poll(()=>sidebar.evaluate(el=>el.scrollTop)).toBe(0);
  await expect(page.getByRole('navigation').getByRole('button',{name:'학습 대시보드',exact:true})).toBeInViewport();
  // Enlarged menu text and a smaller dynamic viewport retain the scroll region.
  await page.addStyleTag({content:'.sidebar nav button {font-size: 24px; min-height:72px} .sidebar .text-button {font-size:20px}'});
  await page.setViewportSize({width:390,height:400});
  for(let i=0;i<6;i++) await swipe(340,80);
  await expect.poll(()=>visibleInViewport(page,'.sidebar-bottom button:last-of-type')).toBe(true);
  for(let i=0;i<6;i++) await swipe(80,340);
  await expect.poll(()=>sidebar.evaluate(el=>el.scrollTop)).toBe(0);
});

test('전 화면 상단 상시 안내 배너 없음·저장 실패 경고 유지', async({page})=>{
  await page.goto('');
  const nav=async(label:string)=>{
    if(await page.getByRole('button',{name:'메뉴 열기'}).isVisible()) await open(page);
    await page.getByRole('navigation').getByRole('button',{name:label,exact:true}).click();
  };
  for(const label of ['학습 대시보드','실전 모의시험','랜덤 문제풀이','오답노트','북마크','학습 통계','문제은행 관리']) {
    await nav(label);
    await expect(page.locator('.criteria-note')).toHaveCount(0);
    const text=await page.locator('main > :first-child').innerText();
    expect(text).not.toMatch(/비공식|잠정 규칙|공식 출제기준 대조 대기/);
  }
  await page.addInitScript(()=>Storage.prototype.setItem=function(){throw new DOMException('quota','QuotaExceededError')});
  await page.reload();
  await expect(page.getByRole('alert')).toContainText('기록을 저장하지 못했습니다');
});
