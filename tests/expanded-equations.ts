// Independent equations/energy balances, not imported from the Python authoring code.
// Numeric inputs are explicitly in the units stated by each question.
const rad = (deg:number) => deg * Math.PI / 180;
export const expandedEvaluators: Record<string,(v:number[])=>number> = {
  'point-potential': ([q,r])=>9e9*(q/1e6)/r/1e3,
  'coulomb-force': ([a,b,r])=>9e9*(a/1e6)*(b/1e6)/(r*r),
  'electric-energy': ([c,v])=>(c/1e6)*v*v/2*1e3,
  'dielectric-flux': ([er,e])=>8.854e-12*er*(e*1e3)*1e6,
  'field-integral': ([a,x])=>a*x*x/2,
  'sphere-capacitance': ([cm])=>cm*.01*(4*Math.PI*8.854),
  'layered-capacitor': ([a,d1,e1,d2,e2])=>{
    const c1=8.854e-12*e1*a/(d1/1000);
    const c2=8.854e-12*e2*a/(d2/1000);
    return (1/(1/c1+1/c2))*1e12;
  },
  'coax-capacitance': ([ratio])=>1/(Math.log(ratio)/(2*Math.PI*8.854)),
  'wire-flux': ([i,r])=>(4*Math.PI*1e-7)*(i/(2*Math.PI*r))*1e6,
  'parallel-wire-force': ([i1,i2,d])=>((4*Math.PI*1e-7)*i1/(2*Math.PI*d))*i2*1000,
  'magnetic-reluctance': ([a,l,mur])=>l/(mur*4*Math.PI*1e-7*(a/10000))/1000,
  'self-inductance': ([n,r])=>{
    const testCurrent=2,flux=n*testCurrent/r;
    return n*flux/testCurrent*1000;
  },
  'mutual-inductance': ([k,l1,l2])=>Math.sqrt(k*k*l1*l2),
  'faraday-average': ([n,phi1,phi2,t])=>Math.abs(n*(phi2-phi1)/1000/t),
  'magnetic-energy': ([l,i])=>l*i*i/2,
  'wave-speed': ([c,er,mur])=>Math.sqrt(c*c/(er*mur)),
  'demand-factor': ([max,connected])=>100/(connected/max),
  'diversity-factor': ([sum,simultaneous])=>sum/simultaneous,
  'load-factor': ([e,t,max])=>(e/max)/t*100,
  'base-impedance': ([v,s])=>{
    const phaseVoltage=v*1000/Math.sqrt(3);
    const baseCurrent=s*1e6/(Math.sqrt(3)*v*1000);
    return phaseVoltage/baseCurrent;
  },
  'pu-base-conversion': ([old,oldS,newS])=>old/(oldS/newS),
  'three-phase-fault-current': ([s,v])=>(s*1e6)/(1.732*v*1000)/1000,
  'single-ground-fault': ([v,z1,z2,z0])=>v/((z1+z2+z0)/3)/1000,
  'ferranti-no-load': ([v,a])=>v*(1/Math.cos(rad(a))),
  'power-angle': ([v1,v2,x,a])=>(v1/x)*(v2*Math.sin(rad(a))),
  'surge-impedance': ([l,c])=>Math.sqrt((l/c)*1000),
  'surge-loading': ([v,z])=>v*(v/z),
  'surge-travel-time': ([l,speed])=>1e6/(speed/l),
  'surge-reflection': ([load,z])=>1-2*z/(load+z),
  'cable-charging': ([c,f,kv])=>(kv*1000/1.732)/(1/(2*Math.PI*f*(c/1e6))),
  'hydro-output': ([q,h,eta])=>9.81*q*h*eta,
  'thermal-plant-efficiency': ([p,m,h])=>(p/m)/h*100,
  'transformer-ratio': ([v,n1,n2])=>v/(n1/n2),
  'transformer-core-resistance': ([v,p])=>v/(p/v),
  'transformer-series-resistance': ([i,p])=>(p/i)/i,
  'transformer-load-copper': ([loss,x])=>loss*x*x,
  'transformer-max-efficiency': ([iron,copper])=>1/Math.sqrt(copper/iron),
  'dc-generator-emf': ([p,phi,z,rpm,paths])=>(rpm/60)*p*phi*(z/paths),
  'dc-motor-back-emf': ([v,r,i])=>v-(r*i),
  'dc-electromagnetic-torque': ([k,i])=>i*k,
  'dc-constant-flux-speed': ([n,e1,e2])=>(n/e1)*e2,
  'transformer-rated-line-current': ([s,v])=>(s*1000/v)/1.732,
  'synchronous-speed': ([hz,p])=>(hz/(p/2))*60,
  'rotor-copper-loss': ([pg,s])=>pg*(s/100),
  'induction-developed-power': ([pg,s])=>pg-pg*s/100,
  'induction-max-torque-slip': ([r,x])=>r/x,
  'pitch-factor': ([a])=>Math.sqrt((1+Math.cos(rad(a)))/2),
  'distribution-factor': ([q,b])=>{
    let re=0,im=0;
    for(let slot=0;slot<q;slot++){re+=Math.cos(rad(slot*b));im+=Math.sin(rad(slot*b));}
    return Math.hypot(re,im)/q;
  },
  'delta-star': ([r])=>r*r/(r+r+r),
  'nodal-voltage': ([v,r1,r2])=>(v/r1)/(1/r1+1/r2),
  'maximum-power-transfer': ([v,r])=>{const i=v/(r+r);return i*i*r;},
  'single-phase-real-power': ([v,i,pf])=>(v*i)*pf,
  'admittance-conductance': ([r,x])=>((r/Math.hypot(r,x))/Math.hypot(r,x))*1000,
  'series-quality-factor': ([w,l,r])=>(w/r)*(l/1000),
  'inductor-initial-slope': ([v,l])=>v/l,
  'zero-sequence-current': v=>v.reduce((sum,i)=>sum+i,0)/3,
  'second-order-settling': ([z,w])=>(1/(z*w))*4,
  'second-order-overshoot': ([z])=>{
    const wd=Math.sqrt(1-z*z),firstPeak=Math.PI/wd;
    return 100*Math.exp(-z*firstPeak);
  },
  'routh-cubic-boundary': ([squared,linear])=>squared*linear,
  'ramp-steady-error': ([k])=>1/k,
  'gain-decibels': ([k])=>10*Math.log10(k*k),
  'lead-maximum-phase': ([a])=>Math.atan((1-a)/(2*Math.sqrt(a)))*180/Math.PI,
  'discrete-pole-radius': ([a,b])=>Math.sqrt(a*a+b*b),
  'laplace-initial-value': ([a])=>a,
  'conductor-adiabatic-area': ([i,t,k])=>Math.sqrt(i*i*t/(k*k)),
  'earth-potential-rise': ([i,r])=>r*i,
  'residual-current': ([out,back])=>Math.abs(out*1000-back*1000),
  'insulation-test-resistance': ([v,micro])=>(v/(micro*1e-6))*1e-6,
  'conductor-temperature-resistance': ([r,a,t])=>r+r*a*(t-20),
  'cable-correction-factors': ([base,temperature,group])=>(base*group)*temperature,
  'ups-battery-capacity': ([wh,v,eff,use])=>((wh/eff)/use)/v,
  'lumen-method-count': ([e,a,f,u,m])=>Math.ceil((e*a/f)/(u*m)),
  'motor-supply-current': ([kw,v,eff,pf])=>((kw*1000/eff)/pf)/v/1.732,
  'flat-energy-charge': ([kw,h,rate])=>(kw*h)*rate,
  'pv-cold-open-circuit': ([n,v,b,t,reference])=>n*(v+v*b*(t-reference)),
  'parallel-insulation': ([r,n])=>1/(n/r),
  'dc-drop-design-length': ([v,percent,a,rho,i])=>{
    const allowed=v*percent/100,loopResistancePerMeter=2*rho/a;
    return (allowed/i)/loopResistancePerMeter;
  },
  'enclosure-thermal-rise': ([p,g])=>p/g,
  'independent-earth-parallel': ([a,b])=>1/(1/a+1/b),
  'capacitor-discharge-time': ([kohm,uf,v,target])=>(kohm*uf/1000)*Math.log(v/target),
};
