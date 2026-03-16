from datetime import datetime

# JEE 2025 Schedule (update dates each year)
JEE_SCHEDULE = [
    {
        "name": "JEE Main 2025 — Session 1",
        "date": datetime(2025, 1, 22),
        "type": "Main",
        "note": "Session 1 begins. Check your city/centre on jeemain.nta.nic.in",
        "subjects": ["Physics", "Chemistry", "Mathematics"],
        "link": "https://jeemain.nta.nic.in"
    },
    {
        "name": "JEE Main 2025 — Session 2",
        "date": datetime(2025, 4, 2),
        "type": "Main",
        "note": "Session 2 — last chance to improve your percentile!",
        "subjects": ["Physics", "Chemistry", "Mathematics"],
        "link": "https://jeemain.nta.nic.in"
    },
    {
        "name": "JEE Advanced 2025",
        "date": datetime(2025, 5, 18),
        "type": "Advanced",
        "note": "Top 2.5L from JEE Main qualify. Paper 1 + Paper 2 on same day.",
        "subjects": ["Physics", "Chemistry", "Mathematics"],
        "link": "https://jeeadv.ac.in"
    },
]

# Resources database
RESOURCES = {
    "physics": {
        "mechanics": [
            {"title": "HC Verma — Mechanics (PDF)", "url": "https://archive.org/details/hcverma", "type": "📄 PDF"},
            {"title": "Concepts of Physics Vol 1 Notes", "url": "https://drive.google.com/drive/folders/physics_mech", "type": "📁 Drive"},
            {"title": "PW — Mechanics Full Playlist", "url": "https://youtube.com/playlist?list=mechanics_pw", "type": "▶️ YouTube"},
        ],
        "optics": [
            {"title": "Ray & Wave Optics — Short Notes", "url": "https://drive.google.com/optics_notes", "type": "📄 PDF"},
            {"title": "JEE Optics PYQs (2015-2024)", "url": "https://drive.google.com/optics_pyq", "type": "📁 Drive"},
            {"title": "Unacademy — Optics Crash Course", "url": "https://youtube.com/optics_crash", "type": "▶️ YouTube"},
        ],
        "electrostatics": [
            {"title": "Electrostatics Formula Sheet", "url": "https://drive.google.com/electro_formula", "type": "📄 PDF"},
            {"title": "DC Pandey Electrostatics Solutions", "url": "https://drive.google.com/dcpandey_electro", "type": "📁 Drive"},
        ],
        "thermodynamics": [
            {"title": "Thermodynamics One-Shot Notes", "url": "https://drive.google.com/thermo_notes", "type": "📄 PDF"},
            {"title": "JEE Thermo PYQs Solved", "url": "https://drive.google.com/thermo_pyq", "type": "📁 Drive"},
        ],
        "general": [
            {"title": "Physics Full Syllabus Notes — JEE", "url": "https://drive.google.com/physics_full", "type": "📁 Drive"},
            {"title": "DC Pandey All Volumes", "url": "https://archive.org/dcpandey", "type": "📄 PDF"},
            {"title": "Physics Wallah JEE Playlist", "url": "https://youtube.com/pw_jee_physics", "type": "▶️ YouTube"},
        ]
    },
    "chemistry": {
        "organic": [
            {"title": "MS Chouhan Organic Chemistry PDF", "url": "https://drive.google.com/ms_chouhan", "type": "📄 PDF"},
            {"title": "Named Reactions Cheat Sheet", "url": "https://drive.google.com/named_reactions", "type": "📄 PDF"},
            {"title": "Vedantu — Organic Reactions Playlist", "url": "https://youtube.com/organic_vedantu", "type": "▶️ YouTube"},
        ],
        "inorganic": [
            {"title": "JD Lee Concise Notes", "url": "https://drive.google.com/jdlee_notes", "type": "📄 PDF"},
            {"title": "Inorganic Chemistry PYQs", "url": "https://drive.google.com/inorg_pyq", "type": "📁 Drive"},
        ],
        "physical": [
            {"title": "Physical Chemistry Formula Booklet", "url": "https://drive.google.com/physchem_formulas", "type": "📄 PDF"},
            {"title": "Narendra Awasthi Solutions", "url": "https://drive.google.com/awasthi", "type": "📁 Drive"},
        ],
        "general": [
            {"title": "NCERT Chemistry Class 11 & 12", "url": "https://ncert.nic.in/textbook.php", "type": "📄 PDF"},
            {"title": "Chemistry Full Notes — JEE", "url": "https://drive.google.com/chem_full", "type": "📁 Drive"},
        ]
    },
    "maths": {
        "calculus": [
            {"title": "Calculus — Limits, Derivatives, Integration Notes", "url": "https://drive.google.com/calculus_notes", "type": "📄 PDF"},
            {"title": "RD Sharma Calculus Solutions", "url": "https://drive.google.com/rdsharma_calc", "type": "📁 Drive"},
        ],
        "algebra": [
            {"title": "Algebra Formula Sheet — JEE", "url": "https://drive.google.com/algebra_formulas", "type": "📄 PDF"},
            {"title": "SK Goyal Algebra PDF", "url": "https://drive.google.com/skgoyal", "type": "📄 PDF"},
        ],
        "coordinate": [
            {"title": "Coordinate Geometry Complete Notes", "url": "https://drive.google.com/coord_geo", "type": "📄 PDF"},
            {"title": "SL Loney Coordinate Geometry", "url": "https://archive.org/slloney", "type": "📄 PDF"},
        ],
        "trigonometry": [
            {"title": "Trigonometry Formula Sheet", "url": "https://drive.google.com/trig_formulas", "type": "📄 PDF"},
            {"title": "SL Loney Trigonometry", "url": "https://archive.org/slloney_trig", "type": "📄 PDF"},
        ],
        "general": [
            {"title": "Maths Full Notes — JEE Mains + Advanced", "url": "https://drive.google.com/maths_full", "type": "📁 Drive"},
            {"title": "Cengage Maths Series PDFs", "url": "https://drive.google.com/cengage_maths", "type": "📄 PDF"},
            {"title": "Unacademy JEE Maths Playlist", "url": "https://youtube.com/maths_unacademy", "type": "▶️ YouTube"},
        ]
    },
    "general": [
        {"title": "JEE Main Previous Year Papers (2015–2024)", "url": "https://drive.google.com/jee_pyp_all", "type": "📁 Drive"},
        {"title": "JEE Advanced PYQs Full Pack", "url": "https://drive.google.com/jeeadv_pyq", "type": "📁 Drive"},
        {"title": "NTA Official Mock Tests", "url": "https://nta.ac.in/mock-tests", "type": "🌐 Website"},
        {"title": "JEE Syllabus 2025 (Official)", "url": "https://jeemain.nta.nic.in/syllabus", "type": "🌐 Website"},
    ]
}

SUBJECTS = ["physics", "chemistry", "maths"]
TOPICS = {
    "physics": ["mechanics", "optics", "electrostatics", "thermodynamics", "general"],
    "chemistry": ["organic", "inorganic", "physical", "general"],
    "maths": ["calculus", "algebra", "coordinate", "trigonometry", "general"]
}
