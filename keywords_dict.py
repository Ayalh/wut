

def acronym_function(x):
    d = {'MATQu': 'computing, technology, qubit', 'HELoS': 'initiative, medical, device, technology', 
     'AFarCloud': 'farming, labour, health, order, project', 'ASTONISH': 'application, imaging, technology', 
     'EXIST': 'image, sensor, imaging, pixel, high, filter, spectral', 'CSA-Industry4.E': 'liase, stakeholder, project', 
     'DENSE': 'system, weather, environment', 'Productive4.0': 'project, industry, solution', 
     'ENABLE-S3': 'system, test, validation', 'MANTIS': 'mantis, maintenance, system', 
     'POSITION-II': 'position, technology, platform', 'Moore4Medical': 'medical, application, technology, platform', 
     'TRANSACT': 'safety, critical, system, service, transact, cloud', 'InSecTT': 'thing, intelligent, secure, system', 
     'InForMed': 'pilot, line, fabrication', 'SCOTT': 'wireless, solution, end, domain, user', 
     'MegaMaRt2': 'productivity, industrial, runtime', 'DELPHI4LED': 'industry, product, market, multi, model, development, tool, compact', 
     '3Ccar': 'project, complexity, semiconductor, innovation', 'PRYSTINE': 'system, fail, operational, fusion', 
     'RobustSENSE': 'system, condition, robustsense', 'EuroPAT-MASIP': '', 'NewControl': 'platform, perception, control, safety', 
     'IMOCO4.E': 'machine, layer, control', 'FRACTAL': 'computing, node, cognitive', 
     'SECREDAS': 'title, security, cross, domain, reliable, dependable, multi, methodology, reference, architecture, component, autonomous, system, high, privacy, protection, functional, safety, operational, performance', 'AutoDrive': 'driving, european, system, autodrive, situation, safe', 
     'NextPerception': 'smart, system, health, wellbeing, solution, project, automotive, intelligence, monitoring', 
     'StorAIge': 'technology, high, performance, power, solution, application', 'REACTION': 'sic, line, power, smart', 
     'AI4DI': 'industry, ai, system', 'Arrowhead Tools': 'digitalisation, automation, tool, engineering', 
     'WInSiC4AP': 'technology, application, tier1', 'iRel40': 'reliability, system, application', 'R3-PowerUP': 'mm, pilot, line, smart, power', 
     'Energy ECS': 'energy, technology, new', 'PROGRESSUS': 'smart, grid, infrastructure, power, station, energy', 
     'BEYOND5': 'radio, technology, soi, pilot', 'YESvGaN': 'yesvgan, low, cost, power, transistor, technology, vertical', 
     'ADACORSA': 'drone, technology, system', 'CONNECT': 'power, energy, grid, order, local', 'GaN4AP': 'gan, power, device', 
     'DAIS': 'new, component, project', 'ArchitectECA2030': 'validation, eca, vehicle, residual, risk', 
     'CHARM': 'manufacturing, industry, technology, sensor', 'COMP4DRONES': 'drone, ecosystem, comp4drone, architecture, application, compositional, platform', 
     'AI-TWILIGHT': 'lighting, product, digital, twin, ai', 'IoSense': 'manufacturing, market, line, sensor', 
     'PIN3S': 'semiconductor, technology, equipment, material', 'AI4CSM': 'mobility, automotive, industry, transition, digital, vehicle',
     'SILENSE': 'smart, acoustic, technology', 'Power2Power': 'power2power, innovation, power, smart, energy, application, key', 
     'MADEin4': 'metrology, productivity, industry, booster, major, challenge', 'FITOPTIVIS': 'objective, low, optimisation', 
     'SC3': 'semiconductor, supply, domain', 'ANDANTE': 'hardware, capability, application', 
     'COSMOS': 'project, ecsel, lighthouse, stakeholder', 'TAKEMI5': 'project, metrology, process, tool', 
     'OSIRIS': 'sic, power, substrate', 'PRIME': 'project, power, technology, design, block, system, iot', 
     'ID2PPAC': 'project, technology, nm, node, device', 'TAPES3': 'project, metrology, device', 
     'TAKE5': 'project, nm, technology, process', 'PowerBase': 'pilot, line, project', 'SeNaTe': 'nm, technology, process', 
     'ADMONT': 'pilot, line, technology, process, smart', 'MICROPRINCE': 'pilot, line, functional, component, technology', 
     'WAKeMeUP': 'project, memory, application, technology', 'APPLAUSE': 'advanced, packaging, manufacturing', 
     'SafeCOP': 'system, wireless, certification', 'TRANSFORM': 'energy, technology, process, new', 
     'SWARMs': 'offshore, vehicle, auvs, rovs', 'WAYTOGO FAST': 'project, technology, fdsoi, nm', 
     'AMASS': 'system, assurance, certification', 'AIDOaRt': 'continuous, development, software', 
     'CPS4EU': 'cps, technology, strategic, industry, european, large', 'IT2': 'project, technology, equipment, system', 
     'VALU3S': 'manufacturer, system, domain, v&v, method, tool', 'iDev40': 'development, process, manufacturing, digital, technology', 
     '5G_GaN2': 'technology, mm, wave', 'AQUAS': 'complexity, system, world, safety, security, performance, industrial', 
     'HiEFFICIENT': 'partner, high, level, system', 'HELIAUS': 'perception, system, thermal', 
     'SemI40': 'electronic, manufacturing, semi40, industry, partner, system', 'EnSO': 'energy, objective, smart', 
     'I-MECH': 'mech, system, motion, speed, control', 'HiPERFORM': 'high, semiconductor, power', 
     '3DAM': 'project, new, metrology, semiconductor, technology', 'VIZTA': 'technology, sensor, source, range, key, smart, filter, integrated', 
     'UltimateGaN': 'power, application, gan, device, efficiency', 'BRAINE': 'edge, computing, braine', 
     'R2POWER300': 'manufacturing, line, mm, new, process, technology, smart, power', 'REFERENCE': 'european, rf, technology', 
     'TARANTO': 'project, high, system', 'TEMPO': 'neuromorphic, dnn, technology', 'OCEAN12': 'fdsoi, technology, low'}
    return d[x]

acronym = 'SafeCOP'
print(acronym, '>>', acronym_function(acronym))