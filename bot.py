import random
import time
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, PollAnswerHandler, MessageHandler, filters, ContextTypes

TOKEN = "8670215239:AAFBNhhAK1-kv-wwdnWHNqWsC0TYL1MreJ4"

# =========================================
# PASTE YOUR QUESTIONS BELOW
# =========================================

physics_questions_base = [

{"question":"Which of the following is SI unit of force?","options":["Newton","Pascal","Joule","Watt"],"answer":0},
{"question":"Momentum of a body depends on","options":["mass and velocity","mass only","velocity only","acceleration"],"answer":0},
{"question":"Dimensional formula of kinetic energy is","options":["MLT⁻²","ML²T⁻²","ML²T⁻¹","MLT⁻¹"],"answer":1},
{"question":"Acceleration due to gravity near Earth surface is","options":["8.9 m/s²","9.8 m/s²","10.8 m/s²","11 m/s²"],"answer":1},
{"question":"Work done by a force is zero when","options":["force is zero","displacement is zero","force ⟂ displacement","all of these"],"answer":3},
{"question":"Unit of pressure is","options":["Joule","Pascal","Watt","Newton"],"answer":1},
{"question":"Escape velocity of Earth is approximately","options":["7.9 km/s","9.8 km/s","11.2 km/s","12.5 km/s"],"answer":2},
{"question":"Unit of frequency is","options":["Tesla","Hertz","Volt","Ampere"],"answer":1},
{"question":"Kinetic energy of a body is proportional to","options":["velocity","velocity²","mass","acceleration"],"answer":1},
{"question":"Newton’s first law is also called","options":["Law of inertia","Law of acceleration","Law of gravitation","Hooke's law"],"answer":0},

{"question":"Ohm’s law is given by","options":["V = IR","V = I/R","R = IV","I = VR"],"answer":0},
{"question":"SI unit of resistance is","options":["Volt","Ampere","Ohm","Tesla"],"answer":2},
{"question":"SI unit of capacitance is","options":["Farad","Henry","Tesla","Weber"],"answer":0},
{"question":"SI unit of magnetic flux is","options":["Tesla","Weber","Henry","Ampere"],"answer":1},
{"question":"Unit of inductance is","options":["Henry","Ohm","Tesla","Volt"],"answer":0},
{"question":"Speed of light in vacuum is","options":["3×10⁸ m/s","3×10⁶ m/s","3×10⁵ m/s","3×10⁷ m/s"],"answer":0},
{"question":"Photoelectric effect was explained by","options":["Einstein","Bohr","Newton","Planck"],"answer":0},
{"question":"Energy of photon is","options":["hf","mv²","mc²","mgh"],"answer":0},
{"question":"SI unit of electric field is","options":["Volt","N/C","Ampere","Joule"],"answer":1},
{"question":"SI unit of charge is","options":["Coulomb","Volt","Ampere","Ohm"],"answer":0},

{"question":"SI unit of magnetic field is","options":["Tesla","Weber","Henry","Volt"],"answer":0},
{"question":"Frequency of AC supply in India is","options":["60 Hz","50 Hz","100 Hz","25 Hz"],"answer":1},
{"question":"Transformer works on the principle of","options":["electromagnetic induction","photoelectric effect","electrostatics","gravitation"],"answer":0},
{"question":"Unit of conductance is","options":["Siemens","Ohm","Volt","Tesla"],"answer":0},
{"question":"Electron was discovered by","options":["Rutherford","Bohr","J.J Thomson","Chadwick"],"answer":2},

{"question":"Gamma rays are","options":["electromagnetic waves","alpha particles","beta particles","neutrons"],"answer":0},
{"question":"Unit of angular velocity is","options":["rad/s","m/s","N","J"],"answer":0},
{"question":"Unit of torque is","options":["N m","J","W","kg"],"answer":0},
{"question":"Unit of Young’s modulus is","options":["Pascal","Joule","Newton","Watt"],"answer":0},
{"question":"Unit of surface tension is","options":["kg","J","N/m","m²"],"answer":2},

{"question":"Unit of entropy is","options":["J","K","J/K","N"],"answer":2},
{"question":"SI unit of luminous intensity is","options":["Candela","Lux","Joule","Watt"],"answer":0},
{"question":"Unit of electric potential is","options":["Volt","Ampere","Ohm","Tesla"],"answer":0},
{"question":"Refractive index is","options":["v/c","c/v","uv","v²"],"answer":1},
{"question":"Mirror formula is","options":["1/f = 1/v + 1/u","f = uv","v = uf","f = u/v"],"answer":0},

{"question":"Unit of electric current is","options":["Ampere","Volt","Tesla","Ohm"],"answer":0},
{"question":"Unit of magnetic permeability is","options":["Henry/m","Tesla","Volt","Ampere"],"answer":0},
{"question":"Bohr model explains","options":["hydrogen spectrum","gravity","elasticity","thermal expansion"],"answer":0},
{"question":"De Broglie wavelength is","options":["h/p","p/h","h²/p","ph"],"answer":0},
{"question":"Compton effect proves","options":["wave nature","particle nature of light","gravity","heat"],"answer":1},

{"question":"SI unit of wavelength is","options":["meter","second","tesla","joule"],"answer":0},
{"question":"Unit of power of lens is","options":["Diopter","Volt","Tesla","Meter"],"answer":0},
{"question":"SI unit of heat is","options":["Joule","Watt","Pascal","Newton"],"answer":0},
{"question":"Unit of thermal conductivity is","options":["W/mK","J","kg","N"],"answer":0},
{"question":"Unit of magnetic dipole moment is","options":["A m²","Tesla","Volt","Henry"],"answer":0},

{"question":"Unit of gravitational constant is","options":["N m²/kg²","kg/m","J/kg","N/m"],"answer":0},
{"question":"Unit of velocity is","options":["m/s","kg","N","J"],"answer":0},
{"question":"Unit of density is","options":["kg/m³","kg","m","kg/m"],"answer":0},
{"question":"Unit of acceleration is","options":["m/s²","m/s","kg","N"],"answer":0},
{"question":"SI unit of power is","options":["Watt","Joule","Newton","Pascal"],"answer":0}
]

chemistry_questions_base = [

# -------- 11th Standard (10 Questions) --------

{"question":"Atomic number of an element represents","options":["number of protons","number of neutrons","atomic mass","number of isotopes"],"answer":0},
{"question":"Avogadro number is","options":["6.022×10^23","6.022×10^20","6.022×10^26","6.022×10^22"],"answer":0},
{"question":"pH of neutral water at 25°C is","options":["5","6","7","8"],"answer":2},
{"question":"The most electronegative element is","options":["Oxygen","Fluorine","Nitrogen","Chlorine"],"answer":1},
{"question":"Which of the following is an alkali metal?","options":["Sodium","Calcium","Aluminium","Iron"],"answer":0},
{"question":"The hybridization of carbon in methane is","options":["sp","sp²","sp³","sp³d"],"answer":2},
{"question":"The gas evolved when zinc reacts with HCl is","options":["Hydrogen","Oxygen","Chlorine","Nitrogen"],"answer":0},
{"question":"Which law states that mass is conserved in a reaction?","options":["Law of multiple proportions","Law of conservation of mass","Gay Lussac law","Avogadro law"],"answer":1},
{"question":"The molar mass of oxygen gas (O₂) is","options":["16 g/mol","18 g/mol","32 g/mol","28 g/mol"],"answer":2},
{"question":"Which of the following is a noble gas?","options":["Neon","Nitrogen","Oxygen","Hydrogen"],"answer":0},

# -------- 12th Standard (40 Questions) --------

{"question":"The unit of molarity is","options":["mol/kg","mol/L","g/L","kg/mol"],"answer":1},
{"question":"Catalyst increases reaction rate by","options":["increasing activation energy","decreasing activation energy","changing equilibrium","changing product"],"answer":1},
{"question":"Electrolysis of water produces","options":["H₂ and O₂","CO₂ and O₂","H₂ and CO₂","O₂ only"],"answer":0},
{"question":"Which acid is a strong acid?","options":["HCl","CH₃COOH","H₂CO₃","HCOOH"],"answer":0},
{"question":"The number of moles in 22.4 L of gas at STP is","options":["0.5","1","2","22.4"],"answer":1},
{"question":"Which of the following is an aldehyde?","options":["CH₃CHO","CH₃COOH","CH₃COCH₃","C₂H₅OH"],"answer":0},
{"question":"Which functional group is present in alcohols?","options":["–OH","–COOH","–CHO","–NH₂"],"answer":0},
{"question":"Which metal is used in galvanization?","options":["Zinc","Iron","Copper","Aluminium"],"answer":0},
{"question":"Which gas is responsible for greenhouse effect?","options":["CO₂","O₂","N₂","He"],"answer":0},
{"question":"Which compound is used as bleaching agent?","options":["Bleaching powder","NaCl","KNO₃","Na₂SO₄"],"answer":0},

{"question":"Which of the following is an example of ester?","options":["CH₃COOC₂H₅","CH₃COOH","CH₃CHO","C₂H₅OH"],"answer":0},
{"question":"The oxidation state of oxygen in H₂O₂ is","options":["-2","-1","0","+1"],"answer":1},
{"question":"Which gas turns lime water milky?","options":["CO₂","O₂","SO₂","N₂"],"answer":0},
{"question":"The process of converting ore to oxide by heating is","options":["Roasting","Calcination","Electrolysis","Distillation"],"answer":0},
{"question":"Which element is used in making fertilizers?","options":["Nitrogen","Helium","Argon","Neon"],"answer":0},

{"question":"Which of the following is an isomer of butane?","options":["Isobutane","Methane","Ethane","Propane"],"answer":0},
{"question":"Which acid is present in vinegar?","options":["Acetic acid","Citric acid","Sulphuric acid","Nitric acid"],"answer":0},
{"question":"Which compound is used in soda water?","options":["CO₂","SO₂","O₂","NH₃"],"answer":0},
{"question":"The main component of LPG is","options":["Butane","Methane","Ethane","Propane"],"answer":3},
{"question":"Which vitamin contains cobalt?","options":["Vitamin B12","Vitamin C","Vitamin A","Vitamin D"],"answer":0},

{"question":"Which of the following is a polymer?","options":["Polyethylene","Methane","Benzene","Ethane"],"answer":0},
{"question":"Which metal is liquid at room temperature?","options":["Mercury","Iron","Copper","Zinc"],"answer":0},
{"question":"The pH of acidic solution is","options":["less than 7","equal to 7","greater than 7","14"],"answer":0},
{"question":"Which of the following is a base?","options":["NaOH","HCl","H₂SO₄","CO₂"],"answer":0},
{"question":"Which gas is used in Haber process?","options":["Nitrogen","Oxygen","Helium","Argon"],"answer":0},

{"question":"Which of the following is aromatic compound?","options":["Benzene","Methane","Ethane","Propane"],"answer":0},
{"question":"Which element has atomic number 1?","options":["Hydrogen","Helium","Oxygen","Nitrogen"],"answer":0},
{"question":"Which compound contains peptide bond?","options":["Protein","Fat","Carbohydrate","Vitamin"],"answer":0},
{"question":"Which of the following is ketone?","options":["CH₃COCH₃","CH₃CHO","CH₃COOH","C₂H₅OH"],"answer":0},
{"question":"Which compound is used in antiseptic solution?","options":["Phenol","Methane","Ethane","Propane"],"answer":0},

{"question":"Which gas is used in manufacture of ammonia?","options":["Hydrogen","Oxygen","CO₂","Helium"],"answer":0},
{"question":"Which compound is used in perfumes?","options":["Esters","Alkanes","Alkenes","Alcohols"],"answer":0},
{"question":"Which acid is present in lemon?","options":["Citric acid","Acetic acid","Sulphuric acid","Nitric acid"],"answer":0},
{"question":"Which of the following is a reducing agent?","options":["H₂","O₂","Cl₂","NO₂"],"answer":0},
{"question":"Which metal is used in batteries?","options":["Lead","Iron","Copper","Silver"],"answer":0}

]
math_questions_base = [

# -------- 11th Standard (20 Questions) --------

{"question":"Value of sin²θ + cos²θ is","options":["0","1","2","sinθ"],"answer":1},
{"question":"Derivative of x² is","options":["x","2x","x²","1"],"answer":1},
{"question":"log10(100) equals","options":["1","2","10","100"],"answer":1},
{"question":"Slope of line y = 3x + 5 is","options":["3","5","8","2"],"answer":0},
{"question":"Value of tan 45° is","options":["0","1","√3","-1"],"answer":1},
{"question":"Number of subsets of a set with 3 elements","options":["6","8","9","4"],"answer":1},
{"question":"Value of cos 0°","options":["0","1","-1","½"],"answer":1},
{"question":"Derivative of sin x","options":["cos x","sin x","tan x","-sin x"],"answer":0},
{"question":"If a matrix has order 2×3, number of elements","options":["6","5","3","2"],"answer":0},
{"question":"Value of log1(10)","options":["undefined","0","1","10"],"answer":0},

{"question":"Distance between points (0,0) and (3,4)","options":["4","5","6","7"],"answer":1},
{"question":"Value of sin 90°","options":["0","1","½","√3"],"answer":1},
{"question":"Value of cos 60°","options":["½","1","0","√3"],"answer":0},
{"question":"Derivative of e^x","options":["e^x","xe","1","0"],"answer":0},
{"question":"Value of tan 0°","options":["0","1","-1","∞"],"answer":0},

{"question":"Angle sum of triangle","options":["90°","180°","360°","270°"],"answer":1},
{"question":"Value of log(1)","options":["1","0","10","undefined"],"answer":1},
{"question":"Derivative of constant","options":["0","1","constant","undefined"],"answer":0},
{"question":"Number of diagonals in square","options":["2","4","6","8"],"answer":0},
{"question":"Value of sin 30°","options":["½","1","0","√3"],"answer":0},

# -------- 12th Standard (80 Questions) --------

{"question":"Integration of 1/x dx","options":["ln x + C","x + C","1/x + C","x² + C"],"answer":0},
{"question":"Derivative of cos x","options":["-sin x","sin x","cos x","tan x"],"answer":0},
{"question":"Determinant of identity matrix","options":["1","0","-1","2"],"answer":0},
{"question":"Value of lim x→0 (sin x / x)","options":["0","1","∞","-1"],"answer":1},
{"question":"If A is 2×2 matrix, determinant gives","options":["scalar","vector","matrix","tensor"],"answer":0},

{"question":"Integration of sin x","options":["-cos x + C","cos x + C","sin x + C","tan x + C"],"answer":0},
{"question":"Derivative of ln x","options":["1/x","x","ln x","0"],"answer":0},
{"question":"Value of cos²θ − sin²θ","options":["cos2θ","sin2θ","tan2θ","1"],"answer":0},
{"question":"Rank of identity matrix of order 3","options":["3","2","1","0"],"answer":0},
{"question":"If probability of event is 0","options":["impossible","certain","equal","random"],"answer":0},

{"question":"Probability range","options":["0 to 1","1 to 10","-1 to 1","0 to 10"],"answer":0},
{"question":"Value of lim x→∞ (1/x)","options":["0","1","∞","-1"],"answer":0},
{"question":"Derivative of tan x","options":["sec²x","tan x","sec x","cot x"],"answer":0},
{"question":"Integration of cos x","options":["sin x + C","cos x + C","-sin x + C","tan x + C"],"answer":0},
{"question":"Derivative of sec x","options":["sec x tan x","sec²x","tan x","cot x"],"answer":0},

{"question":"If A+B = B+A, property is","options":["commutative","associative","identity","inverse"],"answer":0},
{"question":"Determinant value if two rows equal","options":["0","1","2","undefined"],"answer":0},
{"question":"Derivative of x³","options":["3x²","x²","3x","x³"],"answer":0},
{"question":"Integration of e^x","options":["e^x + C","xe","ln x","x²"],"answer":0},
{"question":"Mean of numbers is","options":["average","sum","median","mode"],"answer":0},

{"question":"Variance measures","options":["spread","center","probability","limit"],"answer":0},
{"question":"Standard deviation symbol","options":["σ","π","θ","λ"],"answer":0},
{"question":"Matrix inverse exists if determinant","options":["≠0","=0","=1","=2"],"answer":0},
{"question":"Value of tan 90°","options":["undefined","0","1","∞"],"answer":0},
{"question":"Value of cos 180°","options":["-1","1","0","½"],"answer":0},

{"question":"Derivative of √x","options":["1/(2√x)","√x","2√x","1/x"],"answer":0},
{"question":"Integration of 1 dx","options":["x + C","1/x","ln x","0"],"answer":0},
{"question":"If two events independent","options":["P(A∩B)=P(A)P(B)","P(A)+P(B)","P(A)-P(B)","0"],"answer":0},
{"question":"Mode represents","options":["most frequent value","average","middle","variance"],"answer":0},
{"question":"Median represents","options":["middle value","sum","variance","range"],"answer":0},

{"question":"Derivative of log x","options":["1/x","x","log x","0"],"answer":0},
{"question":"Integration of sec²x","options":["tan x + C","sec x","cos x","cot x"],"answer":0},
{"question":"Derivative of cot x","options":["-cosec²x","sec²x","tan x","cot x"],"answer":0},
{"question":"Value of sin 180°","options":["0","1","-1","½"],"answer":0},
{"question":"Value of cos 90°","options":["0","1","-1","½"],"answer":0},

{"question":"Derivative of 1/x","options":["-1/x²","1/x²","x","0"],"answer":0},
{"question":"Integration of tan x","options":["ln|sec x|","tan x","sec x","cos x"],"answer":0},
{"question":"Derivative of a constant multiple kx","options":["k","x","kx","1"],"answer":0},
{"question":"Slope of vertical line","options":["undefined","0","1","∞"],"answer":0},
{"question":"Slope of horizontal line","options":["0","1","undefined","∞"],"answer":0},

{"question":"If determinant = 0 matrix is","options":["singular","identity","scalar","unit"],"answer":0},
{"question":"Unit matrix determinant","options":["1","0","-1","2"],"answer":0},
{"question":"Integration constant symbol","options":["C","K","A","B"],"answer":0},
{"question":"Derivative of ln(e^x)","options":["1","x","0","e"],"answer":0},
{"question":"Value of tan 30°","options":["1/√3","√3","1","0"],"answer":0},

{"question":"Value of cos 30°","options":["√3/2","½","1","0"],"answer":0},
{"question":"Value of sin 60°","options":["√3/2","½","1","0"],"answer":0},
{"question":"Probability of certain event","options":["1","0","½","2"],"answer":0},
{"question":"Probability of impossible event","options":["0","1","½","-1"],"answer":0},
{"question":"Derivative of x","options":["1","x","0","2"],"answer":0},

{"question":"Integration of 2x","options":["x² + C","2x","x + C","2"],"answer":0},
{"question":"Value of sec 0°","options":["1","0","∞","-1"],"answer":0},
{"question":"Value of cosec 90°","options":["1","0","∞","-1"],"answer":0},
{"question":"Derivative of a² where a constant","options":["0","1","a","a²"],"answer":0},
{"question":"Value of tan 60°","options":["√3","1","0","½"],"answer":0}

]

biology_questions_base = [

{"question":"Basic unit of life","options":["Cell","Atom","Organ","DNA"],"answer":0},
{"question":"Study of plants is called","options":["Botany","Zoology","Ecology","Genetics"],"answer":0},
{"question":"Study of animals is called","options":["Zoology","Botany","Anatomy","Cytology"],"answer":0},
{"question":"Father of genetics","options":["Mendel","Darwin","Pasteur","Lamarck"],"answer":0},
{"question":"Largest organ of human body","options":["Skin","Heart","Brain","Liver"],"answer":0},

{"question":"Human chromosome number","options":["46","23","44","48"],"answer":0},
{"question":"Powerhouse of the cell","options":["Mitochondria","Nucleus","Golgi body","Ribosome"],"answer":0},
{"question":"Green pigment in plants","options":["Chlorophyll","Carotene","Xanthophyll","Anthocyanin"],"answer":0},
{"question":"Process by which plants make food","options":["Photosynthesis","Respiration","Digestion","Fermentation"],"answer":0},
{"question":"Gas used in photosynthesis","options":["CO2","O2","N2","H2"],"answer":0},

{"question":"Gas released during photosynthesis","options":["Oxygen","Nitrogen","Hydrogen","Carbon monoxide"],"answer":0},
{"question":"Genetic material in most organisms","options":["DNA","RNA","Protein","Lipid"],"answer":0},
{"question":"Functional unit of kidney","options":["Nephron","Neuron","Alveoli","Villi"],"answer":0},
{"question":"Largest gland in human body","options":["Liver","Pancreas","Thyroid","Pituitary"],"answer":0},
{"question":"Human heart has chambers","options":["4","2","3","5"],"answer":0},

{"question":"Blood group discovered by","options":["Landsteiner","Darwin","Mendel","Pasteur"],"answer":0},
{"question":"Vitamin produced by sunlight","options":["Vitamin D","Vitamin A","Vitamin C","Vitamin B"],"answer":0},
{"question":"Red blood cell pigment","options":["Hemoglobin","Chlorophyll","Keratin","Melanin"],"answer":0},
{"question":"Largest bone in human body","options":["Femur","Tibia","Humerus","Ulna"],"answer":0},
{"question":"Number of bones in adult human","options":["206","210","300","180"],"answer":0},

{"question":"Study of environment","options":["Ecology","Biology","Genetics","Botany"],"answer":0},
{"question":"Organism that makes its own food","options":["Autotroph","Heterotroph","Parasite","Saprophyte"],"answer":0},
{"question":"Animals that eat plants","options":["Herbivores","Carnivores","Omnivores","Parasites"],"answer":0},
{"question":"Animals that eat flesh","options":["Carnivores","Herbivores","Omnivores","Detritivores"],"answer":0},
{"question":"Animals eating plants and animals","options":["Omnivores","Carnivores","Herbivores","Parasites"],"answer":0},

{"question":"Process of breathing","options":["Respiration","Circulation","Digestion","Excretion"],"answer":0},
{"question":"Human breathing organ","options":["Lungs","Heart","Kidney","Liver"],"answer":0},
{"question":"Liquid part of blood","options":["Plasma","Serum","Lymph","Platelets"],"answer":0},
{"question":"Cells that fight infection","options":["WBC","RBC","Platelets","Plasma"],"answer":0},
{"question":"Blood clotting element","options":["Platelets","RBC","WBC","Serum"],"answer":0},

{"question":"Cell control center","options":["Nucleus","Membrane","Cytoplasm","Cell wall"],"answer":0},
{"question":"Site of protein synthesis","options":["Ribosome","Golgi body","Lysosome","Nucleus"],"answer":0},
{"question":"Cell division producing identical cells","options":["Mitosis","Meiosis","Binary fission","Budding"],"answer":0},
{"question":"Cell division producing gametes","options":["Meiosis","Mitosis","Fragmentation","Budding"],"answer":0},
{"question":"Unit of heredity","options":["Gene","Chromosome","DNA","Allele"],"answer":0},

{"question":"Largest cell in human body","options":["Ovum","RBC","Neuron","Muscle cell"],"answer":0},
{"question":"Plant tissue transporting water","options":["Xylem","Phloem","Cambium","Cortex"],"answer":0},
{"question":"Plant tissue transporting food","options":["Phloem","Xylem","Cambium","Epidermis"],"answer":0},
{"question":"Opening on leaf for gas exchange","options":["Stomata","Node","Petiole","Vein"],"answer":0},
{"question":"Food making part of plant","options":["Leaf","Stem","Root","Flower"],"answer":0},

{"question":"Reproductive part of plant","options":["Flower","Leaf","Stem","Root"],"answer":0},
{"question":"Male reproductive part of flower","options":["Stamen","Carpel","Petal","Sepal"],"answer":0},
{"question":"Female reproductive part of flower","options":["Carpel","Stamen","Petal","Sepal"],"answer":0},
{"question":"Seed develops from","options":["Ovule","Ovary","Anther","Stigma"],"answer":0},
{"question":"Fruit develops from","options":["Ovary","Ovule","Anther","Stigma"],"answer":0},

{"question":"Hormone controlling blood sugar","options":["Insulin","Adrenaline","Thyroxine","Estrogen"],"answer":0},
{"question":"Hormone controlling metabolism","options":["Thyroxine","Insulin","Adrenaline","Testosterone"],"answer":0},
{"question":"Male reproductive hormone","options":["Testosterone","Estrogen","Progesterone","Thyroxine"],"answer":0},
{"question":"Female reproductive hormone","options":["Estrogen","Testosterone","Insulin","Adrenaline"],"answer":0},
{"question":"Energy currency of cell","options":["ATP","DNA","RNA","ADP"],"answer":0},

{"question":"Largest artery in body","options":["Aorta","Pulmonary artery","Carotid","Renal"],"answer":0},
{"question":"Balance of body controlled by","options":["Cerebellum","Cerebrum","Medulla","Hypothalamus"],"answer":0},
{"question":"Thinking part of brain","options":["Cerebrum","Cerebellum","Medulla","Spinal cord"],"answer":0},
{"question":"Water loss from leaves","options":["Transpiration","Respiration","Photosynthesis","Digestion"],"answer":0},
{"question":"Plant hormone for growth","options":["Auxin","Ethylene","Cytokinin","Gibberellin"],"answer":0},

{"question":"Fruit ripening hormone","options":["Ethylene","Auxin","Cytokinin","ABA"],"answer":0},
{"question":"Organ purifying blood","options":["Kidney","Liver","Heart","Lung"],"answer":0},
{"question":"Excretion process removes","options":["Waste","Oxygen","Food","Hormones"],"answer":0},
{"question":"Digestive enzyme for proteins","options":["Pepsin","Amylase","Lipase","Maltase"],"answer":0},
{"question":"Enzyme digesting starch","options":["Amylase","Pepsin","Lipase","Trypsin"],"answer":0},

{"question":"Enzyme digesting fats","options":["Lipase","Pepsin","Amylase","Maltase"],"answer":0},
{"question":"Smallest bone in human body","options":["Stapes","Femur","Tibia","Ulna"],"answer":0},
{"question":"Largest part of brain","options":["Cerebrum","Cerebellum","Medulla","Pons"],"answer":0},
{"question":"Human fertilization occurs in","options":["Fallopian tube","Uterus","Ovary","Cervix"],"answer":0},
{"question":"Embryo develops in","options":["Uterus","Ovary","Fallopian tube","Vagina"],"answer":0},

{"question":"Organism feeding on dead matter","options":["Saprophyte","Parasite","Autotroph","Producer"],"answer":0},
{"question":"Organism living on host","options":["Parasite","Saprophyte","Autotroph","Producer"],"answer":0},
{"question":"Green plants in food chain","options":["Producers","Consumers","Decomposers","Parasites"],"answer":0},
{"question":"Bacteria reproduction","options":["Binary fission","Mitosis","Meiosis","Budding"],"answer":0},
{"question":"Virus genetic material","options":["DNA or RNA","Protein","Lipid","Carbohydrate"],"answer":0},

{"question":"Photosynthesis organelle","options":["Chloroplast","Mitochondria","Golgi","Nucleus"],"answer":0},
{"question":"Human body normal temperature","options":["37°C","35°C","40°C","30°C"],"answer":0},
{"question":"Plant root function","options":["Absorb water","Make food","Respiration","Photosynthesis"],"answer":0},
{"question":"Organ pumping blood","options":["Heart","Lung","Kidney","Liver"],"answer":0},
{"question":"Plant stem function","options":["Transport water","Photosynthesis","Respiration","Digestion"],"answer":0}

]
# =========================================
# DO NOT EDIT BELOW THIS LINE
# =========================================

def expand_questions(base_list, target):
    questions = []
    while len(questions) < target:
        for q in base_list:
            questions.append(q.copy())
            if len(questions) >= target:
                break
    return questions

physics_questions = expand_questions(physics_questions_base,50)
chemistry_questions = expand_questions(chemistry_questions_base,50)
math_questions = expand_questions(math_questions_base,100)
biology_questions = expand_questions(biology_questions_base,100)

subjects = {
    "Physics": physics_questions,
    "Chemistry": chemistry_questions,
    "Maths": math_questions,
    "Biology": biology_questions
}

user_tests = {}
leaderboard = {}
user_stats = {}

# ================= START =================

async def start(update:Update,context:ContextTypes.DEFAULT_TYPE):

    keyboard = [
        ["📝 Practice Mode", "⏱ Exam Mode"],
        ["📊 My Stats", "🏆 Leaderboard"],
        ["ℹ️ Help"]
    ]

    await update.message.reply_text(
        "🎓 MHT CET PRO\n\nSelect an option:",
        reply_markup=ReplyKeyboardMarkup(keyboard,resize_keyboard=True)
    )

# ================= MENU =================

async def menu(update:Update,context:ContextTypes.DEFAULT_TYPE):

    text = update.message.text
    user_id = update.effective_user.id
    name = update.effective_user.first_name

    if user_id not in user_stats:
        user_stats[user_id] = {"name":name,"Physics":0,"Chemistry":0,"Maths":0,"Biology":0}

    if text == "📝 Practice Mode":
        context.user_data["mode"] = "practice"

        keyboard=[["Physics","Chemistry","Maths","Biology"]]
        await update.message.reply_text(
            "📚 Select Subject",
            reply_markup=ReplyKeyboardMarkup(keyboard,resize_keyboard=True)
        )

    elif text == "⏱ Exam Mode":
        context.user_data["mode"] = "exam"

        keyboard=[["PCM","PCB"]]
        await update.message.reply_text(
            "🎯 Select Exam Group",
            reply_markup=ReplyKeyboardMarkup(keyboard,resize_keyboard=True)
        )

    elif text == "PCM":
        keyboard=[["Physics","Chemistry","Maths"]]
        await update.message.reply_text(
            "Select Subject",
            reply_markup=ReplyKeyboardMarkup(keyboard,resize_keyboard=True)
        )

    elif text == "PCB":
        keyboard=[["Physics","Chemistry","Biology"]]
        await update.message.reply_text(
            "Select Subject",
            reply_markup=ReplyKeyboardMarkup(keyboard,resize_keyboard=True)
        )

    elif text == "🏆 Leaderboard":

        if not leaderboard:
            await update.message.reply_text("No data yet.")
            return

        top = sorted(leaderboard.items(), key=lambda x:x[1], reverse=True)[:10]

        msg = "🏆 Top Students\n\n"

        for i,(u,s) in enumerate(top,1):
            name = user_stats[u]["name"]
            msg += f"{i}. {name} : {s}\n"

        await update.message.reply_text(msg)

    elif text == "ℹ️ Help":

        await update.message.reply_text(
            "ℹ️ How to use:\n\n"
            "1. Choose Practice or Exam\n"
            "2. Select subject\n"
            "3. Answer MCQs\n"
            "4. Check score\n\n"
            "🚀 Practice daily!"
        )

    elif text in subjects:

        questions = subjects[text]

        mode = context.user_data.get("mode","practice")

        user_tests[user_id] = {
            "score":0,
            "index":0,
            "questions":questions,
            "subject":text,
            "start_time":time.time(),
            "mode":mode
        }

        await send_question(update.effective_chat.id,context,user_id)

# ================= SEND QUESTION =================

async def send_question(chat_id,context,user_id):

    test = user_tests[user_id]

    index = test["index"]
    total = len(test["questions"])

    mode = test.get("mode","practice")

    if mode == "exam":
        elapsed = time.time() - test["start_time"]
        remaining = int(10800 - elapsed)
    else:
        remaining = (total - index) * 60

    # ✅ FIX: auto submit when time ends
    if remaining <= 0:
        test["index"] = total   # force finish

    if index >= total:

        score = test["score"]
        accuracy = round((score/total)*100,2)

        leaderboard[user_id] = score
        name = user_stats[user_id]["name"]

        await context.bot.send_message(
            chat_id,
            f"""
⏱ Time Up / Test Completed

👤 {name}
📊 Score: {score}/{total}
📈 Accuracy: {accuracy}%
"""
        )

        top = sorted(leaderboard.items(),key=lambda x:x[1],reverse=True)[:5]

        text = "🏆 Leaderboard\n\n"

        for i,(u,s) in enumerate(top,1):
            uname = user_stats[u]["name"]
            text += f"{i}. {uname} : {s}\n"

        await context.bot.send_message(chat_id,text)

        await context.bot.send_message(chat_id,"🔄 Type /start to return to menu")
        return

    q = test["questions"][index]

    options = q["options"].copy()
    correct_option = options[q["answer"]]

    random.shuffle(options)
    new_correct_index = options.index(correct_option)

    minutes = remaining // 60
    seconds = remaining % 60

    await context.bot.send_message(
        chat_id,
        f"⏱ Time Left: {minutes} min {seconds} sec"
    )

    message = await context.bot.send_poll(
        chat_id,
        q["question"],
        options,
        type="quiz",
        correct_option_id=new_correct_index,
        is_anonymous=False
    )

    context.bot_data[message.poll.id] = {
        "user_id": user_id,
        "correct_option": new_correct_index
    }

# ================= RECEIVE ANSWER =================

async def receive_answer(update:Update,context:ContextTypes.DEFAULT_TYPE):

    answer = update.poll_answer
    poll_id = answer.poll_id

    if poll_id not in context.bot_data:
        return

    data = context.bot_data[poll_id]
    user_id = data["user_id"]
    correct_option = data["correct_option"]

    test = user_tests[user_id]
    subject = test.get("subject")

    if answer.option_ids[0] == correct_option:
        test["score"] += 1

        if subject:
            user_stats[user_id][subject] += 1

    test["index"] += 1

    await send_question(answer.user.id,context,user_id)

# ================= STATS =================

async def stats(update:Update,context:ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    if user_id not in user_stats:
        await update.message.reply_text("No test data yet.")
        return

    data = user_stats[user_id]

    total = data["Physics"] + data["Chemistry"] + data["Maths"] + data["Biology"]

    await update.message.reply_text(
        f"""
📊 Your Dashboard

👤 {data["name"]}

🔬 Physics: {data["Physics"]}
⚗️ Chemistry: {data["Chemistry"]}
📐 Maths: {data["Maths"]}
🌿 Biology: {data["Biology"]}

🏆 Total Score: {total}
"""
    )

# ================= RUN =================

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start",start))
app.add_handler(CommandHandler("stats",stats))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,menu))
app.add_handler(PollAnswerHandler(receive_answer))

import time

while True:
    try:
        print("Bot started...")
        app.run_polling()
    except Exception as e:
        print(f"Error: {e}")
        print("Restarting bot in 5 seconds...")
        time.sleep(5)
