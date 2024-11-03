from flask import *
from datetime import *
from flask_sqlalchemy import *
import os
from models import *
app = Flask(__name__)
app.secret_key = "hehe"
app.permanent_session_lifetime = timedelta(minutes=30)

#models
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///master.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

with app.app_context():
    db.init_app(app)



def insertelements():
    
    db.session.add(Elements(1,"H", "Hydrogen", "1.Hydrogen_.jpg", "The lightest and most abundant element in the universe.", "https://www.youtube.com/embed/cxFb4hmfVT0"))
    db.session.add(Elements(2,"He", "Helium", "2.Helium.jpg", "A noble gas that is lighter than air and is used in various applications." , "https://www.youtube.com/embed/hLUcO26Q7wE"))
    db.session.add(Elements(3,"Li", "Lithium", "3.Lithium_.jpg", "A soft, silvery metal used in batteries and various industrial applications."  , "https://www.youtube.com/embed/byGE-bhNzOY"))
    db.session.add(Elements(4,"Be", "Beryllium", "4.Beryllium.jpg","A lightweight metal with high strength-to-weight ratio used in aerospace and defense industries."  , "https://www.youtube.com/embed/GGfkO-2Nh40"))
    db.session.add(Elements(5,"B", "Boron", "5.Boron.jpg","A metalloid element used in the production of glass and ceramics."  , "https://www.youtube.com/embed/PvTSxOh1PDY"))
    db.session.add(Elements(6,"C", "Carbon", "6.Carbon.jpg","The basis of all organic compounds and essential for life." , "https://www.youtube.com/embed/ULiLt2rtpAg"))
    db.session.add(Elements(7,"N", "Nitrogen", "7.Nitrogen.jpg"," A gas that makes up the majority of Earth's atmosphere." , "https://www.youtube.com/embed/IHfqVe8eq4E"))
    db.session.add(Elements(8,"O", "Oxygen", "8.Oxygen.jpg","A reactive gas essential for respiration and combustion." , "https://www.youtube.com/embed/twn_2HQR6fU"))
    db.session.add(Elements(9,"F", "Fluorine", "9.Flourine.jpg","The most reactive of all the elements, used in various applications such as toothpaste." , "https://www.youtube.com/embed/aitIRoDbnIw"))
    db.session.add(Elements(10,"Ne", "Neon", "10.Neon.jpg","- A noble gas commonly used in neon signs." , "https://www.youtube.com/embed/6ev4KHAToWM"))
    db.session.add(Elements(11,"Na", "Sodium", "11.Sodium.jpg","A soft, silvery metal that is highly reactive and essential for life." , "https://www.youtube.com/embed/mf9vZ7uLFQA"))
    db.session.add(Elements(12,"Mg", "Magnesium", "12.Magnesium.jpg","A lightweight metal used in alloys and various industrial applications." , "https://www.youtube.com/embed/hEZmO6qqQww"))
    db.session.add(Elements(13,"Al", "Aluminium", "13.Aluminium.png","A lightweight metal widely used in construction and transportation industries." , "https://www.youtube.com/embed/lLWBE6w_oR4"))
    db.session.add(Elements(14,"Si", "Silicon", "14.Silicon.png","A metalloid essential for the electronics industry." , "https://www.youtube.com/embed/Sq3jgT5fjhg"))
    db.session.add(Elements(15,"P", "Phosporus", "15.Phosporus.png","A non-metal essential for life in the form of phosphate compounds." , "https://www.youtube.com/embed/NdOyFPv7TkY"))
    db.session.add(Elements(16,"S", "Sulfur", "16.Sulfur.jpg","A non-metal used in the production of sulfuric acid and various industrial applications." , "https://www.youtube.com/embed/1ve8cuAq56I"))
    db.session.add(Elements(17,"Cl", "Chlorine", "17.Chlorine.png","A highly reactive gas used in water treatment and the production of PVC." , "https://www.youtube.com/embed/0Ddep5cpDwc"))
    db.session.add(Elements(18,"Ar", "Argon", "18.Argon.jpg","A noble gas used in various applications such as welding and lighting." , "https://www.youtube.com/embed/N0Gw6-xMLlo"))
    db.session.add(Elements(19,"K", "Potassium", "19.Potassium.png","A soft, silvery metal essential for plant and animal life." , "https://www.youtube.com/embed/IQBr9XKstvI"))
    db.session.add(Elements(20,"Ca", "Calcium", "20.Calcium.jpg","A metal essential for bone health and various biological functions." , "https://www.youtube.com/embed/PAU-SqbNsl0"))
    db.session.add(Elements(21,"Sc", "Scandium", "21.Scandium.png","A silvery-white transition metal with applications in aerospace and lighting industries." , "https://www.youtube.com/embed/zwfZHEaBc70"))
    db.session.add(Elements(22,"Ti", "Titanium", "22.Titanium.png","A strong, lightweight transition metal used in aerospace, medical implants, and sports equipment." , "https://www.youtube.com/embed/zFhFq61z2mQ"))
    db.session.add(Elements(23,"V", "Vanadium", "23.Vanadium.png","A transition metal used in the production of steel and various alloys." , "https://www.youtube.com/embed/PEVo9hJvRTg"))
    db.session.add(Elements(24,"Cr", "Chromium", "24.Chromium.png","A hard, shiny transition metal used in stainless steel and decorative coatings." , "https://www.youtube.com/embed/G1g6BtcdrR4"))
    db.session.add(Elements(25,"Mn", "Manganese", "25.Manganese.png","A transition metal used in steel production and batteries." , "https://www.youtube.com/embed/VTlLqD_DojQ"))
    db.session.add(Elements(26,"Fe", "Iron", "26.Iron.jpg","A crucial transition metal for human health and the most widely used metal on Earth." , "https://www.youtube.com/embed/uAMMQv0rKFI"))
    db.session.add(Elements(27,"Co", "Cobalt", "27.Cobalt.jpg","A transition metal used in rechargeable batteries, magnets, and industrial applications." , "https://www.youtube.com/embed/2ihJ_GaSHfI"))
    db.session.add(Elements(29,"Cu", "Copper", "29.Copper.jpg","A reddish-brown transition metal known for its excellent electrical conductivity and use in wiring and plumbing." , "https://www.youtube.com/embed/gqmkiPPIsUQ"))
    db.session.add(Elements(28,"Ni", "Nickel", "28.Nickel.jpg","A silvery-white transition metal used in alloys, batteries, and plating." , "https://www.youtube.com/embed/tUKeQXzzpYk"))
    db.session.add(Elements(30,"Zn", "Zinc", "30.Zinc.jpg","A bluish-white transition metal used in galvanizing, batteries, and various alloys." , "https://www.youtube.com/embed/ju6gGLxq99k"))
    db.session.add(Elements(31,"Ga", "Gallium", "31.Gallium.jpg","A soft, silvery metal with a low melting point used in electronics and LEDs." , "https://www.youtube.com/embed/g_VYf8MdVSw"))
    db.session.add(Elements(32,"Ge", "Germanium", "32.Germanium.png","A metalloid used in semiconductors and fiber optics." , "https://www.youtube.com/embed/2xylv_hijXw"))
    db.session.add(Elements(33,"As", "Arsenic", "33.Arsenic.png","A metalloid with toxic properties and limited industrial applications." , "https://www.youtube.com/embed/7hUw6_t_Y4o"))
    db.session.add(Elements(34,"Se", "Selenium", "34.Selenium.jpg","A non-metal used in electronics, glassmaking, and as a dietary supplement." , "https://www.youtube.com/embed/IHrUtKjcAFE"))
    db.session.add(Elements(35,"Br", "Bromine", "35.Bromine.jpg","A reddish-brown liquid halogen used in flame retardants and pharmaceuticals." , "https://www.youtube.com/embed/nuW_VbKdvMI"))
    db.session.add(Elements(36,"Kr", "Krypton", "36.Krypton.png","A noble gas used in lighting and laser applications." , "https://www.youtube.com/embed/PWKdzef-ANU"))
    db.session.add(Elements(37,"Rb", "Rubidium", "37.Rubidium.png","A soft, silvery metal used in research and specialty glasses." , "https://www.youtube.com/embed/g0P-A23m3lE"))
    db.session.add(Elements(38,"Sr", "Strontium", "38.Strontium.png","A soft, silvery metal used in pyrotechnics and medical imaging." , "https://www.youtube.com/embed/rrDJ8Ri3pXk"))
    db.session.add(Elements(39,"Y", "Yttrium", "39.Yttrium.png","A transition metal used in alloys, lasers, and phosphors." , "https://www.youtube.com/embed/pzWKE_0wOdM"))
    db.session.add(Elements(40,"Zr", "Zirconium", "40.Zirconium.png","A corrosion-resistant transition metal used in nuclear reactors, aerospace, and medical implants." , "https://www.youtube.com/embed/ooie1JwD5Cg"))
    db.session.add(Elements(41,"Nb", "Niobium", "41.Niobium.png","A shiny transition metal used in superalloys for jet engines and in nuclear reactors." , "https://www.youtube.com/embed/K90HPbVZOQ4"))
    db.session.add(Elements(42,"Mo", "Molybdenum", "42.Molybdenum.png","A transition metal used in high-strength alloys, lubricants, and catalysts." , "https://www.youtube.com/embed/QWW67ZxJ73k"))
    db.session.add(Elements(43,"Tc", "Technitium", "43.Technitium.jpg","A synthetic element with various radioactive isotopes used in medical imaging." , "https://www.youtube.com/embed/6mhDUuljEkE"))
    db.session.add(Elements(44,"Ru", "Ruthenium", "44.Ruthenium.png","A rare transition metal used in electrical contacts, coatings, and catalysts." , "https://www.youtube.com/embed/xtY6BpT4DTY"))
    db.session.add(Elements(45,"Rh", "Rhodium", "45.Rhodium.jpg","A rare transition metal known for its use in catalytic converters and jewelry." , "https://www.youtube.com/embed/t_iMqO89npo"))
    db.session.add(Elements(46,"Pd", "Palladium", "46.Palladium.jpg","A precious metal used in catalytic converters, electronics, and jewelry." , "https://www.youtube.com/embed/UPXzbyY9nL0"))
    db.session.add(Elements(47,"Ag", "Silver", "47.Silver.jpg","A precious metal valued for its beauty and conductivity, used in jewelry and currency." , "https://www.youtube.com/embed/jRwUmGpmF38"))
    db.session.add(Elements(48,"Cd", "Cadmium", "48.Cadmium.png","A toxic transition metal used in batteries, pigments, and coatings." , "https://www.youtube.com/embed/J3XjitEH2oU"))
    db.session.add(Elements(49,"In", "Indium", "49.Indium.jpg","A soft, malleable metal used in electronics, solar panels, and touchscreens." , "https://www.youtube.com/embed/TviX7V-ay5I"))
    db.session.add(Elements(51,"Sb", "Antimony", "51.Antimony.jpg","A metalloid used in flame retardants, batteries, and semiconductors." , "https://www.youtube.com/embed/Tf0hPi3uj5c"))
    db.session.add(Elements(52,"Te", "Tellurium", "52.Tellurium.jpg","A metalloid used in alloys, solar panels, and electronic devices." , "https://www.youtube.com/embed/HH79V-FZqCU"))
    db.session.add(Elements(53,"I", "Iodine", "53.Iodine.jpg","A halogen essential for thyroid function and used in pharmaceuticals and dyes." , "https://www.youtube.com/embed/1UiZYvzkY0o"))
    db.session.add(Elements(50,"Sn", "Tin", "50.Tin.jpg","A malleable metal used in alloys, coatings, and solder." , "https://www.youtube.com/embed/Q9zdt-rOB0Y"))
    db.session.add(Elements(54,"Xe", "Xenon", "54.Xenon.jpg","A noble gas used in lighting, anesthesia, and laser technology." , "https://www.youtube.com/embed/Y7Xes6LV6zE"))
    db.session.add(Elements(55,"Cs", "Caesium", "55.Caesium.jpg","A soft, silvery metal used in atomic clocks, drilling fluids, and medical devices." , "https://www.youtube.com/embed/46eKJDFmVHg"))
    db.session.add(Elements(56,"Ba", "Barium", "56.Barium.jpg","A soft, silvery metal used in drilling fluids, medical imaging, and fireworks." , "https://www.youtube.com/embed/dtWVaYXD9xA"))
    db.session.add(Elements(57,"La", "Lanthanium", "57.Lanthanium.jpg","A rare earth metal used in catalysts, hybrid car batteries, and camera lenses." , "https://www.youtube.com/embed/dwjsqpgzpcM"))
    db.session.add(Elements(58,"Ce", "Cerium", "58.Cerium.jpg","A rare earth metal used in catalytic converters, glass polishing, and alloys." , "https://www.youtube.com/embed/HSa9MvYc90E"))
    db.session.add(Elements(59,"Pr", "Praseodymium", "59.Praseodymium.jpg","A rare earth metal used in magnets, lasers, and glass coloring." , "https://www.youtube.com/embed/FHDb-VjDWeE"))
    db.session.add(Elements(60,"Nd", "Neodymium", "60.Neodymium.jpg","A rare earth metal used in high-strength magnets, lasers, and headphones." , "https://www.youtube.com/embed/BDwIc-plsYQ"))
    db.session.add(Elements(61,"Pm", "Promethium", "61.Promethium.jpg","A radioactive element that does not exist in nature and is typically only found in laboratories." , "https://www.youtube.com/embed/9-HvNj2FRO4"))
    db.session.add(Elements(62,"Sm", "Samarium", "62.Samarium.jpg","Another rare earth metal used in magnets and nuclear reactors." , "https://www.youtube.com/embed/aDh8-l7DDbM"))
    db.session.add(Elements(64,"Gd", "Gadolinium", "64.Gadolinium.jpg","A rare earth metal with applications in medical imaging and neutron capture therapy." , "https://www.youtube.com/embed/EXbtlgva32Y"))
    db.session.add(Elements(65,"Tb", "Terbium", "65.Terbium.jpg","A rare earth metal used in electronic devices and phosphors." , "https://www.youtube.com/embed/On5LjH9TQxY"))
    db.session.add(Elements(63,"Eu", "Europium", "63.Europium.jpg","A rare earth metal used in phosphors for displays and in nuclear reactors." , "https://www.youtube.com/embed/PNl1xsPp6ro"))
    db.session.add(Elements(66,"Dy", "Dysprosium", "66.Dysprosium.jpg","A rare earth metal used in magnets, lasers, and nuclear control rods." , "https://www.youtube.com/embed/uc4EVhl-EuY"))
    db.session.add(Elements(67,"Ho", "Holmium", "67.Holmium.jpg","A rare earth metal used in nuclear control rods and some medical devices." , "https://www.youtube.com/embed/v5CNMTfWVJ8"))
    db.session.add(Elements(68,"Er", "Erbium", "68.Erbium.jpg","A rare earth metal used in optical fibers, lasers, and nuclear reactors." , "https://www.youtube.com/embed/zJ7SfFTUqgQ"))
    db.session.add(Elements(69,"Tm", "Thulium", "69.Thulium.jpg","A rare earth metal used in portable X-ray machines and lasers." , "https://www.youtube.com/embed/vS0vhYdOGMc"))
    db.session.add(Elements(70,"Yb", "Ytterbium", "70.Ytterbium.jpg","A rare earth metal used in medical devices, lasers, and atomic clocks." , "https://www.youtube.com/embed/LGAmrFTr5e4"))
    db.session.add(Elements(71,"Lu", "Lutetium", "71.Lutetium.jpg","A rare earth metal with applications in catalysts and cancer treatment." , "https://www.youtube.com/embed/7wrDfRnRHqI"))
    db.session.add(Elements(72,"Hf", "Hafnium", "72.Hafnium.png","A metal often used in nuclear reactors and in superalloys for jet engines." , "https://www.youtube.com/embed/-jLX2D_tta0"))
    db.session.add(Elements(73,"Ta", "Tantalum", "73.Tantalum.jpg","A metal known for its resistance to corrosion and used in electronic components." , "https://www.youtube.com/embed/7tsiT_zdFew"))
    db.session.add(Elements(74,"W", "Tungsten", "74.Tungsten.jpg","A metal with the highest melting point of any element and used in high-temperature applications." , "https://www.youtube.com/embed/6XxcVg2Dfck"))
    db.session.add(Elements(75,"Re", "Rhenium", "75.Rhenium.jpg","A rare metal used in high-temperature superalloys and catalysts." , "https://www.youtube.com/embed/Duk20wEVgJQ"))
    db.session.add(Elements(76,"Os", "Osmium", "76.Osmium.jpg","A dense metal often used in alloys for fountain pen tips and electrical contacts." , "https://www.youtube.com/embed/D9C_lbivcn4"))
    db.session.add(Elements(77,"Ir", "Iridium", "77.Iridium.jpg","A dense, corrosion-resistant metal used in spark plugs, electrical contacts, and in some jewelry." , "https://www.youtube.com/embed/lGy1vGnYAak"))
    db.session.add(Elements(78,"Pt", "Platinum", "78.Platinum.jpg","A precious metal used in jewelry, catalytic converters, and various industrial applications." , "https://www.youtube.com/embed/vhPu-3b0FnY"))
    db.session.add(Elements(79,"Au", "Gold", "79.Gold.jpg","A precious metal known for its beauty and used in jewelry, electronics, and as a financial asset." , "https://www.youtube.com/embed/nuNVbfy9Wig"))
    db.session.add(Elements(80,"Hg", "Mercury", "80.Mercury.jpg","A heavy, toxic metal that is liquid at room temperature and historically used in thermometers and barometers." , "https://www.youtube.com/embed/oL0M_6bfzkU"))
    db.session.add(Elements(81,"Tl", "Thallium", "81.Thallium.jpg","A toxic metal used in electronic devices, optical lenses, and in some medical treatments." , "https://www.youtube.com/embed/ZvgrXJwMm8I"))
    db.session.add(Elements(82,"Pb", "Lead", "82.Lead.jpg","A heavy metal used in batteries, construction, and various industrial applications." , "https://www.youtube.com/embed/LjpthO4r1GY"))
    db.session.add(Elements(83,"Bi", "Bismuth", "83.Bismuth.jpg","A heavy metal used in cosmetics, pharmaceuticals, and in some low-melting alloys." , "https://www.youtube.com/embed/0YDDPILNQ5I"))
    db.session.add(Elements(84,"Po", "Polonium", "84.Polonium.jpg","A highly radioactive element that occurs in uranium ores and is used in some industrial applications." , "https://www.youtube.com/embed/K97oJed15j0"))
    db.session.add(Elements(85,"At", "Astatine", "85.Astatine.jpg","A highly radioactive halogen element that is extremely rare and has no significant commercial applications. It is typically only found in trace amounts in uranium and thorium ores." , "https://www.youtube.com/embed/AirrYWYpVIY"))
    db.session.add(Elements(86,"Rn", "Radon", "86.Radon.jpg","A radioactive noble gas that is colorless, odorless, and tasteless. It is formed as a decay product of uranium and thorium, and it is a health hazard due to its radioactivity." , "https://www.youtube.com/embed/5_I6vj-lXNM"))
    db.session.add(Elements(87,"Fr", "Francium", "87.Francium.jpg","A highly radioactive alkali metal that is extremely rare and has the lowest electronegativity of all the elements. It is very unstable and has a very short half-life." , "https://www.youtube.com/embed/K-yxtbar-8A"))
    db.session.add(Elements(88,"Ra", "Radium", "88.Radium.jpg","A highly radioactive alkaline earth metal that is found in uranium ores. It glows in the dark due to its radioactivity and was once used in self-luminous paints." , "https://www.youtube.com/embed/tlktxXC-ggY"))
    db.session.add(Elements(89,"Ac", "Actinium", "89.Actinium.png","A radioactive element that is the first member of the actinide series. It is used in radiation therapy for cancer treatment and in some scientific research." , "https://www.youtube.com/embed/-C0D6XpDROg"))
    db.session.add(Elements(90,"Th", "Thorium", "90.Thorium.jpg","A naturally occurring radioactive metal that is slightly radioactive. It is used in nuclear reactors as a fuel and in some high-temperature applications." , "https://www.youtube.com/embed/GFAnjEEwPNo"))
    db.session.add(Elements(91,"Pa", "Protactinium", "91.Protactinium.jpg","A radioactive element that is part of the actinide series. It has no significant commercial applications and is primarily used for scientific research." , "https://www.youtube.com/embed/E0rZ8U6LJB0"))
    db.session.add(Elements(92,"U", "Uranium", "92.Uranium.jpg","A radioactive metal that is used primarily as a fuel in nuclear reactors and for nuclear weapons. It has various isotopes, with uranium-235 being the most common fissile isotope." , "https://www.youtube.com/embed/OlOy9vTBGr0"))
    db.session.add(Elements(93,"Np", "Neptunium", "93.Neptunium.jpg","A synthetic radioactive element that is produced in nuclear reactors and is used in some types of nuclear weapons and scientific research." , "https://www.youtube.com/embed/FOfSf3sieeo"))
    db.session.add(Elements(94,"Pu", "Plutonium", "94.Plutonium.jpg","A synthetic radioactive element that is primarily produced in nuclear reactors and used in nuclear weapons and as a fuel in some types of nuclear reactors." , "https://www.youtube.com/embed/l_QgTI1bJgU"))
    db.session.add(Elements(95,"Am", "Americium", "95.Americium.jpg","A synthetic radioactive element that is used in smoke detectors and in some industrial gauges. It is also used in some medical applications." , "https://www.youtube.com/embed/TDF6j8piKco"))
    db.session.add(Elements(96,"Cm", "Curium", "96.Curium.jpg","A synthetic radioactive element that is used in research and in some types of nuclear reactors. It is named after Marie and Pierre Curie." , "https://www.youtube.com/embed/3qS-CKIoRoE"))
    db.session.add(Elements(97,"Bk", "Berkelium", "97.Berkelium.jpg","A synthetic radioactive element that is used in scientific research and has no significant commercial applications." , "https://www.youtube.com/embed/vm13388yQO4"))
    db.session.add(Elements(98,"Cf", "Californium", "98.Californium.jpg","A synthetic radioactive element that is used in neutron sources and for scientific research." , "https://www.youtube.com/embed/ZhvRmbpkx9U"))
    db.session.add(Elements(99,"Es", "Einsteinium", "99.Einsteinium.jpg","A synthetic radioactive element that is named after Albert Einstein. It is produced in nuclear reactors and used in scientific research." , "https://www.youtube.com/embed/vaKtdnYuvDo"))
    db.session.add(Elements(100,"Fm", "Fermium", "100.Fermium.jpg","A synthetic radioactive element that is named after Enrico Fermi. It is produced in nuclear reactors and used in scientific research." , "https://www.youtube.com/embed/9ow8-BLxT2o"))
    db.session.add(Elements(101,"Md", "Mendelivium", "101.Mendelivium.jpg","A synthetic radioactive element named after Dmitri Mendeleev, the creator of the periodic table. It is produced in nuclear reactors and used in scientific research." , "https://www.youtube.com/embed/dJ72elHClD0"))
    db.session.add(Elements(102,"No", "Nobelium", "102.Nobelium.jpg","A synthetic radioactive element named after Alfred Nobel. It is produced in nuclear reactors and used in scientific research." , "https://www.youtube.com/embed/-TSGlvwN404"))
    db.session.add(Elements(103,"Lr", "Lawrencium", "103.Lawrencium.png","A synthetic radioactive element named after Ernest O. Lawrence. It is produced in nuclear reactors and used in scientific research." , "https://www.youtube.com/embed/uZZGEg8aEQI"))
    db.session.add(Elements(104,"Rf", "Rutherfordium", "104.Rutherfordium.jpg","A synthetic radioactive element named after Ernest Rutherford. It is produced in nuclear reactors and has no significant commercial applications." , "https://www.youtube.com/embed/7u9n06ZYz9E"))
    db.session.add(Elements(105,"Db", "Dubnium", "105.Dubnium.jpg","A synthetic radioactive element named after the Russian city of Dubna. It is produced in nuclear reactors and used in scientific research." , "https://www.youtube.com/embed/aFjgfd8pQEo"))
    db.session.add(Elements(106,"Sg", "Seaborgium", "106.Seaborgium.jpg","A synthetic radioactive element named after Glenn T. Seaborg. It is produced in nuclear reactors and used in scientific research." , "https://www.youtube.com/embed/fPLcgyP0UKc"))
    db.session.add(Elements(107,"Bh", "Bohrium", "107.Bohrium.jpg","A synthetic radioactive element named after Niels Bohr. It is produced in nuclear reactors and used in scientific research." , "https://www.youtube.com/embed/hN4ckihvPL4"))
    db.session.add(Elements(108,"Hs", "Hassium", "108.Hassium.webp","A synthetic radioactive element named after the German state of Hesse. It is produced in nuclear reactors and used in scientific research." , "https://www.youtube.com/embed/iNzR5XJTY2Y"))
    db.session.add(Elements(109,"Mt", "Meitnerium", "109.Meitnerium.jpg","A synthetic radioactive element named after Lise Meitner. It is produced in nuclear reactors and used in scientific research." , "https://www.youtube.com/embed/8PWiaAtiNPI"))
    db.session.add(Elements(111,"Rg", "Roentgenium", "111.roentgenium.jpg","A synthetic radioactive element named after Wilhelm Conrad Roentgen. It is produced in nuclear reactors and used in scientific research." , "https://www.youtube.com/embed/HqmXxk43oMc"))
    db.session.add(Elements(112,"Cn", "Copernicium", "112.Copernicium.jpg","A synthetic element named after Nicolaus Copernicus. It is highly radioactive and has no known biological role." , "https://www.youtube.com/embed/S3n_DBNMoqY"))
    db.session.add(Elements(110,"Ds", "Darmstadtium", "110.Darmstadtium.jpg","A synthetic radioactive element named after the German city of Darmstadt. It is produced in nuclear reactors and used in scientific research." , "https://www.youtube.com/embed/lhvMqva3-7M"))
    db.session.add(Elements(113,"Nh", "Nihonium", "113.Nihonium.jpg","A synthetic element named after Japan, where it was discovered. It is highly radioactive and has no significant commercial applications." , "https://www.youtube.com/embed/GeRk-OhSTfI"))
    db.session.add(Elements(114,"Fl", "Flerovium", "114.Flerovium.jpg","A synthetic element named after the Flerov Laboratory of Nuclear Reactions in Russia. It is highly radioactive and has no known biological role." , "https://www.youtube.com/embed/Ub_IZkkKUHI"))
    db.session.add(Elements(115,"Mc", "Moscovium", "115.Moscovium.jpg","A synthetic element named after Moscow, where it was discovered. It is highly radioactive and has no known biological role." , "https://www.youtube.com/embed/DB7GmWrGptg"))
    db.session.add(Elements(116,"Lv", "Livermorium", "116.Livermorium.jpg","A synthetic element named after the Lawrence Livermore National Laboratory in the United States. It is highly radioactive and has no known biological role." , "https://www.youtube.com/embed/XJJNebuLAww"))
    db.session.add(Elements(117,"Ts", "Tennessine", "117.Tennessine.jpg","A synthetic element named after the state of Tennessee. It is highly radioactive and has no known biological role." , "https://www.youtube.com/embed/NJio-gOe6jg"))
    db.session.add(Elements(118,"Og", "Oganesson", "118.Oganesson.jpg","A synthetic element named after Yuri Oganessian. It is the heaviest element on the periodic table and is highly radioactive." , "https://www.youtube.com/embed/dmg5-Hjl0jE "))
    
    
    


#controllers
    
@app.before_request
def create_tables():
    db.create_all()
    db.session.commit()

@app.route("/")
def home():
    #print(Elements.query.filter_by(atomicnum=1).first().__repr__()["num"])
    #print(all)
    #db.session.add(newacc)

    
    try:
        db.session.commit()
    
        return redirect(url_for("login"))
    except:
        print("An error has occured")
        return redirect(url_for("login"))
    
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    #checks if user is already in session    
    #if not, authenticate
    
    print("hehe")
    if "currentuser" in session:
            return redirect(url_for("lobby", user = session["currentuser"]["ign"]))

    if request.method == "POST":
        mode = request.form["mode"]
            
            #checks what form it came from
            # login or signin
        if mode == "login":
            username = request.form["login-username"]
            passwo = request.form["login-password"]            

            authenticate = Students.query.filter_by(firstname = username, password = passwo).first()
                

            if authenticate:

                    
                session["currentuser"] = {
                    "ign": authenticate.ign,
                    "mastery": authenticate.mastery,
                    "level": authenticate.level,
                    "usertype":authenticate.usertype 
                }
                if authenticate.usertype == "teacher":
                        return redirect(url_for("teacher"))
                print(authenticate.firstname)
                    #redirect  to lobby page

                return redirect(url_for("lobby", user = authenticate.firstname))
            else: 
                flash("The account doesn't exists!", "info")
                return render_template("login.html", model = "true")
                
        elif mode == "signin":
                #signup
                #checks if passwords match
            username = request.form["signup-username"]
            password = request.form["signup-password"]
            confirmpassword = request.form["signup-confirmpassword"]
            ign = request.form["signup-ign"]

            alluser = Students.query.filter_by(firstname = username).all()
            alling = Students.query.filter_by(firstname = ign).all()

                #check if user already exists
            if alluser:
                flash("Username already existed!!", "signin")
                return render_template("login.html",model="false") 
            
            if alling:
                flash("IGN already existed!!", "signin")
                return render_template("login.html",model="false") 
                            
            
                #create new account
                
            newuser = Students(username, password, confirmpassword, ign,0,0,"student")
            db.session.add(newuser)
            db.session.commit()

            get_flashed_messages(category_filter="signin").clear()
            flash("Account registered!!", "signin")
                
        return render_template("login.html",model="true")
    return render_template("login.html",model="true")


@app.route("/teacher")
def teacher():
    if "currentuser" in session:
        if session["currentuser"]["usertype"] == "teacher":
            allavg = []
            timeavg = []
            accuracyavg = []
            for i in range(1,13):
                hello = Result.query.filter_by(level = i).all()
                lvl1scores = []

                for i in hello:
                    lvl1scores.append(int(i.score))
                
                if len(lvl1scores) != 0:
                    avg1 = sum(lvl1scores)/len(lvl1scores)
                    allavg.append(avg1)
                else: 
                    allavg.append(0)

            for i in range(1,13):
                hello = Result.query.filter_by(level = i).all()
                lvl1scores = []

                for i in hello:
                    lvl1scores.append(int(i.time))
                
                if len(lvl1scores) != 0:
                    avg1 = sum(lvl1scores)/len(lvl1scores)
                    timeavg.append(avg1)
                else: 
                    timeavg.append(0)
            
            for i in range(1,13):
                hello = Result.query.filter_by(level = i).all()
                lvl1scores = []

                for i in hello:
                    lvl1scores.append(int(i.accuracy))
                
                if len(lvl1scores) != 0:
                    avg1 = sum(lvl1scores)/len(lvl1scores)
                    accuracyavg.append(avg1)
                else: 
                    accuracyavg.append(0)
            
            totalaccounts = len(Students.query.all())
            accounts = Students.query.all()
            sorted = insertion_sort_mastery(accounts)
            sortedaccounts = []
            for i in sorted:
                sortedaccounts.append(
                    {
                        "name":i.ign,
                        "mastery":i.mastery
                    }
                )

            sortedlvl = insertion_sort_level(accounts)
            sortedaccountslvl = []
            for i in sortedlvl:
                sortedaccountslvl.append(
                    {
                        "name":i.ign,
                        "mastery":i.level
                    }
                )

            totalattempts = len(Result.query.all())
            newavgdict = {
                "score":{            
                    "1" : allavg[0],
                    "2" : allavg[1],
                    "3" : allavg[2],
                    "4" : allavg[3],
                    "5" : allavg[4],
                    "6" : allavg[5],
                    "7" : allavg[6],
                    "8" : allavg[7],
                    "9" : allavg[8],
                    "10" : allavg[9],
                    "11" : allavg[10],
                    "12" : allavg[11]
                },
                "time":{            
                    "1" : timeavg[0],
                    "2" : timeavg[1],
                    "3" : timeavg[2],
                    "4" : timeavg[3],
                    "5" : timeavg[4],
                    "6" : timeavg[5],
                    "7" : timeavg[6],
                    "8" : timeavg[7],
                    "9" : timeavg[8],
                    "10" : timeavg[9],
                    "11" : timeavg[10],
                    "12" : timeavg[11]
                },
                "accuracy":{            
                    "1" : accuracyavg[0],
                    "2" : accuracyavg[1],
                    "3" : accuracyavg[2],
                    "4" : accuracyavg[3],
                    "5" : accuracyavg[4],
                    "6" : accuracyavg[5],
                    "7" : accuracyavg[6],
                    "8" : accuracyavg[7],
                    "9" : accuracyavg[8],
                    "10" : accuracyavg[9],
                    "11" : accuracyavg[10],
                    "12" : accuracyavg[11]
                },
                "totaluser": totalaccounts,
                "totalattempts":totalattempts,
                "leadbymastery":sortedaccounts,
                "leadbylvl":sortedaccountslvl
            }
            return render_template("statististics.html",avg = newavgdict)
        return redirect(url_for("login"))
    return redirect(url_for("login"))

@app.route("/teachercredits")
def teachercredits():
    if "currentuser" in session:
        print(session["currentuser"]["usertype"])
        if session["currentuser"]["usertype"] == "teacher":
            return render_template("creds.html")
        return redirect(url_for("login"))
    return redirect(url_for("login"))

@app.route("/<user>")
def lobby(user):
    aluser = Students.query.all()
    for i in aluser:
        print(i.password, i.firstname)

    if "currentuser" in session:
        if user == session["currentuser"]["ign"]:  
            info = [] 
            for i in range (0,118):
                newlement = Elements.query.filter_by(atomicnum = i+1).first()  
                newJSON = {
                    "atomicnum": newlement.atomicnum,
                    "name": newlement.name,
                    "symbol": newlement.symbol,
                    "yt": str(newlement.yt),
                    "trivia": newlement.trivia,
                    "image": newlement.image
                }
                info.append(newJSON)    

            print(info[0])
            return render_template("lobby.html", mastery = session["currentuser"]["mastery"], level = session["currentuser"]["level"], elementinfo = info, ign = session["currentuser"]["ign"])   
        else:
            return redirect(url_for("login"))  
    else:        
        return redirect(url_for("login"))

@app.route("/levels", methods = ["POST", "GET"])
def levels():
    if "currentuser" in session:     
            
            if request.method == "POST":
                lvl = request.form["level"]
                print(lvl)
                return redirect(url_for("takelevel", levelnum = lvl))


            return render_template("levels.html") 
        
    return redirect(url_for("login"))

@app.route("/logout")
def logout():

    session.pop("currentuser", None)
    get_flashed_messages().clear()
    return redirect(url_for("login", model = "false"))

@app.route("/level/<levelnum>", methods = ["POST", "GET"])
def takelevel(levelnum):
    if request.method == "POST":
        answers = [request.form["0"],request.form["1"],request.form["2"],request.form["3"],request.form["4"],request.form["5"],request.form["6"],request.form["7"],request.form["8"],request.form["9"]]
        scors = 0
        for i in range(0, 10):
            print(answers[i], session["questions"][i]["answer"], session["questions"][i]["questionobj"])
            if str(answers[i]).lower() == str(session["questions"][i]["answer"]).lower():
                scors += 1
        
        newstud = Students.query.filter_by(ign = session["currentuser"]["ign"]).first()
        print(newstud.firstname, "HEHEHE")
        newstud.mastery += random.randint(scors, (scors*3))
        newstud.level = int((newstud.mastery / 100) + 1)
        db.session.commit()
        session["currentuser"] = {
                     "ign": newstud.ign,
                     "mastery": newstud.mastery,
                     "level": newstud.level
                }
        
        newResult = Result(levelnum, int(scors*10),scors,session["currentuser"]["ign"], request.form["totalseconds"])
        db.session.add(newResult)
        db.session.commit()

        return render_template('result.html', score = str(scors), accuracy = int(scors*10), time = request.form["timetaken"], level = f"/{levelnum}") 
    
    #session.pop("currentquestions", None)
    if int(levelnum) > 12:
        return redirect(url_for("levels"))

    atomicIndex = []
    first = (10 * (int(levelnum) - 1)) + 1
    second = (int(levelnum)*10)+1
    questions = []
    for i in range(first, second):
        if i > 118:
            atomicIndex.append(int(i)-2)
        else:
            atomicIndex.append(i)

    for i in atomicIndex:

        print(i)
        newlement = Elements.query.filter_by(atomicnum = i).first()
        newquestion = QuestionByElement(newlement)
        

        newJSON = {
            "question": newquestion.question,
            "questionobj": newquestion.questionobj,
            "answer": newquestion.answer,
            "imagelink": str(newquestion.imagelink),
            "hasChoices": newquestion.isMultiple,
            "choices": newquestion.other,
            "hasPic": newquestion.hasPic
        }      
        questions.append(newJSON)
        
    questions = random.sample(questions, k=10)
    session["questions"] = questions

    
        

    return render_template("level.html", content = questions) 

@app.route("/result")
def result():
    return render_template("result.html")

def insertion_sort_mastery(array):
    sorted = [array[0]]
    pointer = array[1]
    for i in range(1 , len(array)):
        indexofhighest = 0
        for a in range(0, len(sorted)):

            if int(array[i].mastery) > int(sorted[a].mastery):
                indexofhighest = a
        sorted.insert(indexofhighest + 1, array[i])
    return sorted

def insertion_sort_level(array):
    sorted = [array[0]]
    pointer = array[1]
    for i in range(1 , len(array)):
        indexofhighest = 0
        for a in range(0, len(sorted)):

            if int(array[i].level) > int(sorted[a].level):
                indexofhighest = a
        sorted.insert(indexofhighest + 1, array[i])
    return sorted


@app.route("/stats")
def stats():
    allavg = []
    timeavg = []
    accuracyavg = []
    for i in range(1,13):
        hello = Result.query.filter_by(level = i).all()
        lvl1scores = []

        for i in hello:
            lvl1scores.append(int(i.score))
        
        if len(lvl1scores) != 0:
            avg1 = sum(lvl1scores)/len(lvl1scores)
            allavg.append(avg1)
        else: 
            allavg.append(0)

    for i in range(1,13):
        hello = Result.query.filter_by(level = i).all()
        lvl1scores = []

        for i in hello:
            lvl1scores.append(int(i.time))
        
        if len(lvl1scores) != 0:
            avg1 = sum(lvl1scores)/len(lvl1scores)
            timeavg.append(avg1)
        else: 
            timeavg.append(0)
    
    for i in range(1,13):
        hello = Result.query.filter_by(level = i).all()
        lvl1scores = []

        for i in hello:
            lvl1scores.append(int(i.accuracy))
        
        if len(lvl1scores) != 0:
            avg1 = sum(lvl1scores)/len(lvl1scores)
            accuracyavg.append(avg1)
        else: 
            accuracyavg.append(0)
    
    totalaccounts = len(Students.query.all())
    accounts = Students.query.all()
    sorted = insertion_sort_mastery(accounts)
    sortedaccounts = []
    for i in sorted:
        sortedaccounts.append(
            {
                "name":i.ign,
                "mastery":i.mastery
            }
        )

    sortedlvl = insertion_sort_level(accounts)
    sortedaccountslvl = []
    for i in sortedlvl:
        sortedaccountslvl.append(
            {
                "name":i.ign,
                "mastery":i.level
            }
        )

    totalattempts = len(Result.query.all())
    newavgdict = {
        "score":{            
            "1" : allavg[0],
            "2" : allavg[1],
            "3" : allavg[2],
            "4" : allavg[3],
            "5" : allavg[4],
            "6" : allavg[5],
            "7" : allavg[6],
            "8" : allavg[7],
            "9" : allavg[8],
            "10" : allavg[9],
            "11" : allavg[10],
            "12" : allavg[11]
        },
        "time":{            
            "1" : timeavg[0],
            "2" : timeavg[1],
            "3" : timeavg[2],
            "4" : timeavg[3],
            "5" : timeavg[4],
            "6" : timeavg[5],
            "7" : timeavg[6],
            "8" : timeavg[7],
            "9" : timeavg[8],
            "10" : timeavg[9],
            "11" : timeavg[10],
            "12" : timeavg[11]
        },
        "accuracy":{            
            "1" : accuracyavg[0],
            "2" : accuracyavg[1],
            "3" : accuracyavg[2],
            "4" : accuracyavg[3],
            "5" : accuracyavg[4],
            "6" : accuracyavg[5],
            "7" : accuracyavg[6],
            "8" : accuracyavg[7],
            "9" : accuracyavg[8],
            "10" : accuracyavg[9],
            "11" : accuracyavg[10],
            "12" : accuracyavg[11]
        },
        "totaluser": totalaccounts,
        "totalattempts":totalattempts,
        "leadbymastery":sortedaccounts,
        "leadbylvl":sortedaccountslvl
    }


    return render_template("monitor.html", avg = newavgdict)

@app.route("/credits")
def credits():
    return render_template("credits.html")

@app.route("/forgot", methods = ["POST","GET"])
def forgot():

    if request.method == "POST":
        username = request.form["username"]
        newpassword = request.form["newpassword"]
        oldpass = request.form["oldpassword"]

        founduser = Students.query.filter_by(firstname = username, password = oldpass).first()
        if founduser:
            founduser.password = newpassword
            db.session.commit()
            return render_template("forgotpass.html", foundba="Account password changed")
        else:
            return render_template("forgotpass.html", foundba="Account not found!!")

    return render_template("forgotpass.html", foundba="")


if __name__ == "__main__":    
    app.run()


