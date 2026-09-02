"""
Guram Magularia — Legal Counsel
Digital resume / personal website built with Dash.

Run:
    pip install -r requirements.txt
    python app.py
    → http://127.0.0.1:8050

The site is bilingual. Every piece of text lives in CONTENT below, once
under "en" and once under "ka" (Georgian). The button in the header swaps
between them by changing the URL to /?lang=ka and back.

Layout and styling live in assets/styles.css and assets/site.js.
"""

from dash import Dash, dcc, html, Input, Output, State, ClientsideFunction

# =========================================================
# 1. CONTENT — edit everything here
# =========================================================

# Shared by both languages — no translation needed.
COMMON = {
    "cv_file": "CV - Guram Magularia.pdf",   # the PDF in /assets
    "hero_bg": "background1.jpg",            # backdrop photo in /assets
    "photo": "profile.jpg",                 # portrait shown in the contact card
    "email": "guram.magularia@gmail.com",
    "phone": "+995 555 12 34 56",
    "phone_href": "+995555123456",
    "linkedin": "https://www.linkedin.com/in/gurammagularia",
    "linkedin_label": "linkedin.com/in/gurammagularia",
}

CONTENT = {

    # =====================================================
    # ENGLISH
    # =====================================================
    "en": {
        "html_lang": "en",
        "switch_label": "ქარ",          # text on the language button
        "switch_title": "ქართულად ნახვა",
        "switch_to": "ka",

        "first_name": "Guram",
        "last_name": "Magularia",
        "role": "Legal Counsel",
        "location": "Tbilisi, Georgia",
        "specialties": ["Civil & Legal Law", "Contract & Business Law",
                        "Real Estate Law"],
        "lede": "Providing strategic legal solutions with precision, integrity, "
                "and a commitment to your success.",
        "about_lead": "Legal counsel with seven years across Real Estate Development "
                      "and Banking Litigation and now leading a Legal Department.",
        "about": "Hands-on ownership of the full legal function — from drafting and "
                 "negotiating high-value contracts to managing litigation and running "
                 "due diligence on multi-million-dollar real estate transactions. "
                 "Experienced in advising executive leadership on legal strategy, "
                 "compliance and business expansion.",

        # (icon, headline value, supporting label)
        "stats": [
            ("fa-solid fa-briefcase", "7+", "Years of Experience"),
            ("fa-solid fa-gavel", "50+", "Cases Handled"),
            ("fa-solid fa-building", "Real Estate", "& Banking Sectors"),
            ("fa-solid fa-users", "Corporate &", "Individual Clients"),
        ],

        "hero_facts": [
            ("Currently", "Head of Legal Department, NEXT"),
            ("Since", "2021"),
            ("Focus", "Real Estate · Contracts · Disputes"),
            ("Languages", "Georgian · English · Russian"),
        ],

        "focus_now": [
            "Legal lead on ongoing real estate development projects",
            "Drafting and negotiating high-value commercial contracts",
            "Managing litigation and dispute resolution",
            "Legal due diligence on property acquisitions",
            "Advising leadership on compliance and expansion",
        ],

        "expertise": [
            ("fa-solid fa-house-chimney", "Real Estate & Development Law",
             "Transactions, leases and property disputes for a leading developer."),
            ("fa-solid fa-file-signature", "Contract Drafting & Negotiation",
             "High-value agreements aligned to Georgian and international standards."),
            ("fa-solid fa-scale-balanced", "Litigation & Dispute Resolution",
             "Court and administrative proceedings, settlements and enforcement."),
            ("fa-solid fa-briefcase", "Corporate & Business Law",
             "Structuring, governance and day-to-day advisory for the business."),
            ("fa-solid fa-shield-halved", "Regulatory Compliance",
             "Keeping operations aligned with the regulatory framework."),
            ("fa-solid fa-magnifying-glass-chart", "Legal Due Diligence",
             "Risk review on multi-million-dollar real estate transactions."),
        ],

        "experience": [
            {
                "role": "Head of Legal Department",
                "org": "NEXT — Real Estate Developer Company",
                "date": "2021 – Present",
                "points": [
                    "Led the legal department of a top real estate development "
                    "company, providing expert guidance on contractual, regulatory, "
                    "and dispute resolution matters.",
                    "Negotiated and drafted high-value contracts, ensuring compliance "
                    "with Georgian and international legal standards.",
                    "Managed litigation and dispute resolution processes, minimizing "
                    "company risks and financial exposure.",
                    "Advised executive leadership on legal strategies, compliance, "
                    "and business expansion initiatives.",
                    "Successfully handled legal due diligence for multi-million-dollar "
                    "real estate transactions.",
                ],
                "tags": ["Real Estate", "Contracts", "Due Diligence",
                         "Team Leadership"],
            },
            {
                "role": "Litigation Lawyer",
                "org": "PASHA Bank Georgia",
                "date": "2021",
                "points": [
                    "Established and led the bank's litigation system.",
                    "Managed legal disputes and enforcement proceedings.",
                    "Advised management on litigation risks and strategies.",
                ],
                "tags": ["Banking", "Litigation", "Enforcement"],
            },
            {
                "role": "Lawyer",
                "org": "FINCA Bank Georgia",
                "date": "2019 – 2021",
                "points": [
                    "Represented the bank in court proceedings and before "
                    "administrative bodies.",
                    "Negotiated settlements and agreements with clients.",
                ],
                "tags": ["Banking", "Court Representation", "Settlements"],
            },
            {
                "role": "Intern",
                "org": "Tbilisi City Court",
                "date": "2018 – 2019",
                "points": [
                    "Assisted the judge and judicial assistant in case proceedings.",
                    "Recorded legal documents and drafted court decisions.",
                    "Performed various procedural and administrative tasks.",
                ],
                "tags": ["Judiciary", "Legal Drafting"],
            },
        ],

        "education": [
            {
                "degree": "Master of Laws (LL.M.)",
                "school": "Tbilisi State University",
                "date": "2016 – 2018",
                "note": "Civil and business law specialisation.",
            },
            {
                "degree": "Bachelor of Laws (LL.B.)",
                "school": "Tbilisi State University",
                "date": "2012 – 2016",
                "note": "Graduated with honours.",
            },
        ],

        # (skill, proficiency label shown on the right, bar fill 0-100)
        "skills": [
            ("Contract Drafting & Negotiation", "Expert", 95),
            ("Civil & Commercial Litigation", "Expert", 90),
            ("Real Estate Transactions", "Expert", 92),
            ("Corporate Governance", "Advanced", 85),
            ("Regulatory Compliance", "Advanced", 88),
        ],

        "soft_skills": [
            "Legal Research", "Risk Assessment", "Client Advisory", "Due Diligence",
            "Mediation", "Team Leadership", "Legal Writing", "Case Strategy",
        ],

        "languages": [
            ("Georgian", "Native", 100),
            ("English", "Professional — C1", 85),
            ("Russian", "Advanced — B2/C1", 80),
        ],

        "licenses": [
            ("fa-solid fa-certificate", "Bar Admission — Georgia",
             "Licensed to practise law, Georgian Bar Association."),
            ("fa-solid fa-award", "Certified Mediator",
             "Accredited in commercial and civil mediation."),
            ("fa-solid fa-book-open", "Real Estate Law Certification",
             "Advanced programme in property and development law."),
            ("fa-solid fa-shield-halved", "Corporate Compliance Training",
             "Regulatory compliance and anti-corruption standards."),
        ],

        "hobbies": [
            ("fa-solid fa-futbol", "Football",
             "A committed supporter, match days included."),
            ("fa-solid fa-hand-fist", "Boxing",
             "Discipline, footwork and a good way to switch off."),
            ("fa-solid fa-person-swimming", "Swimming",
             "Laps in the pool to reset between long cases."),
        ],

        "news": [
            {
                "date": "Legislation of Georgia",
                "title": "Legal Status of Aliens",
                "excerpt": "This Law is intended to establish legal guarantees for "
                           "aliens and stateless persons in Georgia.",
                "url": "https://matsne.gov.ge/en/document/view/2278806?publication=22",
            },
            {
                "date": "Legislation of Georgia",
                "title": "Civil Procedure Code of Georgia",
                "excerpt": "Common Courts of Georgia shall review civil matters under "
                           "the procedures determined by this Code.",
                "url": "https://matsne.gov.ge/en/document/view/29962?publication=177",
            },
            {
                "date": "Legislation of Georgia",
                "title": "Law of Georgia on Entrepreneurs",
                "excerpt": "This Law regulates the legal forms of an entrepreneur and "
                           "the procedures for their incorporation and registration.",
                "url": "https://matsne.gov.ge/en/document/view/5230186?publication=13",
            },
        ],

        "nav": [
            ("Home", "#home"),
            ("Expertise", "#practice"),
            ("Experience", "#experience"),
            ("Education", "#education"),
            ("Skills", "#skills"),
            ("Languages", "#languages"),
            ("Licenses", "#licenses"),
            ("Hobbies", "#hobbies"),
            ("News", "#news"),
            ("Contact", "#contact"),
        ],

        # Interface labels
        "ui": {
            "about_label": "About",
            "schedule": "Schedule consultation",
            "download_cv": "Download CV",
            "expertise_title": "Expertise",
            "expertise_sub": "Where business, property and civil law meet — and "
                             "what I handle day to day.",
            "right_now": "Right now",
            "highlights": "Experience highlights",
            "contact_card": "Contact",
            "view_full": "View full experience",
            "experience_title": "Experience",
            "experience_sub": "Seven years advising banks, developers and "
                              "private clients.",
            "education_title": "Education",
            "skills_title": "Skills",
            "skills_panel": "Legal expertise",
            "strengths_panel": "Core strengths",
            "languages_title": "Languages",
            "licenses_title": "Licenses & Certifications",
            "hobbies_title": "Hobbies",
            "hobbies_sub": "Life outside the office.",
            "news_title": "News & Insights",
            "news_sub": "Georgian legislation that most often affects my clients.",
            "read_note": "Read the law",
            "contact_title": "Contact",
            "get_in_touch": "Get in touch",
            "appointment": "Consultations by appointment, Monday to Friday.",
            "form_title": "Request a consultation",
            "label_name": "Your name",
            "ph_name": "Full name",
            "label_email": "Email",
            "ph_email": "you@example.com",
            "label_message": "How can I help?",
            "ph_message": "A short description of your matter.",
            "send": "Send request",
            "rights": "All rights reserved.",
            "menu": "Open menu",
            "theme": "Switch between light and dark mode",
            "back_to_top": "Back to top",
            "listen": "Listen to this",
            "stop_listening": "Stop",
        },

        # Read aloud by the speaker button in the header.
        "speech": "Welcome to the personal website of Guram, Legal "
                  "Counsel, with Seven years of practice across real estate development "
                  "and banking litigation. If you are looking for considered legal "
                  "solutions, you have come to the right place.",

        # Strings the mail-draft function needs (see assets/site.js)
        "mail": {
            "subject": "Consultation Request",
            "label_name": "Name of the Client",
            "label_message": "How can I help?",
            "m_fill": "Please add your ",
            "f_name": "name",
            "f_email": "email",
            "f_message": "message",
            "m_bad_email": "That email address doesn't look right.",
            "m_opening": "Opening your email app — press send there to deliver "
                         "the request.",
        },
    },

    # =====================================================
    # GEORGIAN — ქართული
    # =====================================================
    "ka": {
        "html_lang": "ka",
        "switch_label": "ENG",
        "switch_title": "View in English",
        "switch_to": "en",

        "first_name": "გურამ",
        "last_name": "მაღულარია",
        "role": "იურიდიული მრჩეველი",
        "location": "თბილისი, საქართველო",
        "specialties": ["სამოქალაქო სამართალი", "ხელშეკრულებისა და ბიზნეს სამართალი",
                        "უძრავი ქონების სამართალი"],
        "lede": "სტრატეგიული იურიდიული გადაწყვეტები სიზუსტით, კეთილსინდისიერებით "
                "და თქვენი წარმატებისადმი ერთგულებით.",
        "about_lead": "იურიდიული მრჩეველი შვიდწლიანი გამოცდილებით უძრავი ქონების "
                      "დეველოპმენტსა და საბანკო სამართალწარმოებაში, ამჟამად "
                      "ხელმძღვანელობს იურიდიულ დეპარტამენტს.",
        "about": "სრული იურიდიული ფუნქციის მართვა — მაღალი ღირებულების "
                 "ხელშეკრულებების შედგენიდან და მოლაპარაკებიდან სამართალწარმოების "
                 "მართვამდე და მრავალმილიონიანი უძრავი ქონების გარიგებების "
                 "იურიდიულ დიუ დილიჯენსამდე. გამოცდილება აღმასრულებელი "
                 "ხელმძღვანელობისთვის იურიდიულ სტრატეგიაზე, შესაბამისობასა და "
                 "ბიზნესის გაფართოებაზე კონსულტაციის გაწევაში.",

        "stats": [
            ("fa-solid fa-briefcase", "7+", "წლიანი გამოცდილება"),
            ("fa-solid fa-gavel", "50+", "წარმოებული საქმე"),
            ("fa-solid fa-building", "უძრავი ქონება", "და საბანკო სფერო"),
            ("fa-solid fa-users", "კორპორაციული", "და კერძო კლიენტები"),
        ],

        "hero_facts": [
            ("ამჟამად", "იურიდიული დეპარტამენტის უფროსი, NEXT"),
            ("პოზიციაზე", "2021 წლიდან"),
            ("ფოკუსი", "უძრავი ქონება · ხელშეკრულებები · დავები"),
            ("ენები", "ქართული · ინგლისური · რუსული"),
        ],

        "focus_now": [
            "მიმდინარე უძრავი ქონების პროექტების იურიდიული ხელმძღვანელობა",
            "მაღალი ღირებულების კომერციული ხელშეკრულებების შედგენა და მოლაპარაკება",
            "სამართალწარმოებისა და დავების მართვა",
            "ქონების შეძენის იურიდიული დიუ დილიჯენსი",
            "ხელმძღვანელობისთვის შესაბამისობასა და გაფართოებაზე კონსულტაცია",
        ],

        "expertise": [
            ("fa-solid fa-house-chimney", "უძრავი ქონებისა და დეველოპმენტის სამართალი",
             "გარიგებები, იჯარა და ქონებრივი დავები წამყვანი დეველოპერისთვის."),
            ("fa-solid fa-file-signature", "ხელშეკრულებების შედგენა და მოლაპარაკება",
             "მაღალი ღირებულების შეთანხმებები ქართული და საერთაშორისო სტანდარტების "
             "შესაბამისად."),
            ("fa-solid fa-scale-balanced", "სამართალწარმოება და დავების გადაწყვეტა",
             "სასამართლო და ადმინისტრაციული წარმოება, მორიგება და აღსრულება."),
            ("fa-solid fa-briefcase", "კორპორაციული და ბიზნეს სამართალი",
             "სტრუქტურირება, მმართველობა და ყოველდღიური იურიდიული მხარდაჭერა."),
            ("fa-solid fa-shield-halved", "მარეგულირებელი შესაბამისობა",
             "საქმიანობის შესაბამისობა მარეგულირებელ ჩარჩოსთან."),
            ("fa-solid fa-magnifying-glass-chart", "იურიდიული დიუ დილიჯენსი",
             "რისკების შეფასება მრავალმილიონიან უძრავი ქონების გარიგებებზე."),
        ],

        "experience": [
            {
                "role": "იურიდიული დეპარტამენტის უფროსი",
                "org": "NEXT — უძრავი ქონების დეველოპერული კომპანია",
                "date": "2021 – დღემდე",
                "points": [
                    "წამყვანი უძრავი ქონების დეველოპერული კომპანიის იურიდიული "
                    "დეპარტამენტის ხელმძღვანელობა, საკონტრაქტო, მარეგულირებელ და "
                    "დავებთან დაკავშირებულ საკითხებზე კონსულტაცია.",
                    "მაღალი ღირებულების ხელშეკრულებების მოლაპარაკება და შედგენა "
                    "ქართული და საერთაშორისო სამართლებრივი სტანდარტების დაცვით.",
                    "სამართალწარმოებისა და დავების მართვა კომპანიის რისკებისა და "
                    "ფინანსური ზარალის მინიმიზაციით.",
                    "აღმასრულებელი ხელმძღვანელობისთვის იურიდიულ სტრატეგიაზე, "
                    "შესაბამისობასა და ბიზნესის გაფართოებაზე კონსულტაცია.",
                    "მრავალმილიონიანი უძრავი ქონების გარიგებების იურიდიული დიუ "
                    "დილიჯენსის წარმატებით განხორციელება.",
                ],
                "tags": ["უძრავი ქონება", "ხელშეკრულებები", "დიუ დილიჯენსი",
                         "გუნდის ხელმძღვანელობა"],
            },
            {
                "role": "სამართალწარმოების იურისტი",
                "org": "PASHA Bank Georgia",
                "date": "2021",
                "points": [
                    "ბანკის სამართალწარმოების სისტემის ჩამოყალიბება და ხელმძღვანელობა.",
                    "სამართლებრივი დავებისა და აღსრულების წარმოების მართვა.",
                    "მენეჯმენტისთვის სამართალწარმოების რისკებსა და სტრატეგიაზე "
                    "კონსულტაცია.",
                ],
                "tags": ["საბანკო", "სამართალწარმოება", "აღსრულება"],
            },
            {
                "role": "იურისტი",
                "org": "FINCA Bank Georgia",
                "date": "2019 – 2021",
                "points": [
                    "ბანკის წარმომადგენლობა სასამართლოსა და ადმინისტრაციულ ორგანოებში.",
                    "კლიენტებთან მორიგებისა და შეთანხმებების მოლაპარაკება.",
                ],
                "tags": ["საბანკო", "სასამართლო წარმომადგენლობა", "მორიგება"],
            },
            {
                "role": "სტაჟიორი",
                "org": "თბილისის საქალაქო სასამართლო",
                "date": "2018 – 2019",
                "points": [
                    "მოსამართლისა და სასამართლოს თანაშემწის დახმარება საქმის "
                    "წარმოებაში.",
                    "სამართლებრივი დოკუმენტების აღრიცხვა და სასამართლო "
                    "გადაწყვეტილებების პროექტების მომზადება.",
                    "სხვადასხვა საპროცესო და ადმინისტრაციული დავალების შესრულება.",
                ],
                "tags": ["მართლმსაჯულება", "იურიდიული წერა"],
            },
        ],

        "education": [
            {
                "degree": "სამართლის მაგისტრი (LL.M.)",
                "school": "თბილისის სახელმწიფო უნივერსიტეტი",
                "date": "2016 – 2018",
                "note": "სამოქალაქო და ბიზნეს სამართლის სპეციალიზაცია.",
            },
            {
                "degree": "სამართლის ბაკალავრი (LL.B.)",
                "school": "თბილისის სახელმწიფო უნივერსიტეტი",
                "date": "2012 – 2016",
                "note": "დაამთავრა წარჩინებით.",
            },
        ],

        "skills": [
            ("ხელშეკრულებების შედგენა და მოლაპარაკება", "ექსპერტი", 95),
            ("სამოქალაქო და კომერციული სამართალწარმოება", "ექსპერტი", 90),
            ("უძრავი ქონების გარიგებები", "ექსპერტი", 92),
            ("კორპორაციული მმართველობა", "მაღალი", 85),
            ("მარეგულირებელი შესაბამისობა", "მაღალი", 88),
        ],

        "soft_skills": [
            "იურიდიული კვლევა", "რისკის შეფასება", "კლიენტთა კონსულტაცია",
            "დიუ დილიჯენსი", "მედიაცია", "გუნდის ხელმძღვანელობა",
            "იურიდიული წერა", "საქმის სტრატეგია",
        ],

        "languages": [
            ("ქართული", "მშობლიური", 100),
            ("ინგლისური", "პროფესიული — C1", 85),
            ("რუსული", "მაღალი — B2/C1", 80),
        ],

        "licenses": [
            ("fa-solid fa-certificate", "ადვოკატთა ასოციაციის წევრი — საქართველო",
             "ლიცენზირებული ადვოკატი, საქართველოს ადვოკატთა ასოციაცია."),
            ("fa-solid fa-award", "სერტიფიცირებული მედიატორი",
             "აკრედიტებული კომერციულ და სამოქალაქო მედიაციაში."),
            ("fa-solid fa-book-open", "უძრავი ქონების სამართლის სერტიფიკატი",
             "გაღრმავებული პროგრამა ქონებისა და დეველოპმენტის სამართალში."),
            ("fa-solid fa-shield-halved", "კორპორაციული შესაბამისობის ტრენინგი",
             "მარეგულირებელი შესაბამისობა და ანტიკორუფციული სტანდარტები."),
        ],

        "hobbies": [
            ("fa-solid fa-futbol", "ფეხბურთი",
             "ერთგული გულშემატკივარი, მატჩების დღეების ჩათვლით."),
            ("fa-solid fa-hand-fist", "კრივი",
             "დისციპლინა, ტექნიკა და კარგი გზა გადასართავად."),
            ("fa-solid fa-person-swimming", "ცურვა",
             "აუზში ცურვა ხანგრძლივ საქმეებს შორის აღსადგენად."),
        ],

        "news": [
            {
                "date": "საქართველოს კანონმდებლობა",
                "title": "უცხოელთა და მოქალაქეობის არმქონე პირთა სამართლებრივი "
                         "მდგომარეობის შესახებ",
                "excerpt": "",
                "url": "https://matsne.gov.ge/ka/document/view/2278806?publication=23",
            },
            {
                "date": "საქართველოს კანონმდებლობა",
                "title": "საქართველოს სამოქალაქო საპროცესო კოდექსი",
                "excerpt": "",
                "url": "https://matsne.gov.ge/ka/document/view/29962?publication=178",
            },
            {
                "date": "საქართველოს კანონმდებლობა",
                "title": "მეწარმეთა შესახებ",
                "excerpt": "",
                "url": "https://matsne.gov.ge/ka/document/view/5230186?publication=13",
            },
        ],

        "nav": [
            ("მთავარი", "#home"),
            ("ექსპერტიზა", "#practice"),
            ("გამოცდილება", "#experience"),
            ("განათლება", "#education"),
            ("უნარები", "#skills"),
            ("ენები", "#languages"),
            ("ლიცენზიები", "#licenses"),
            ("ჰობი", "#hobbies"),
            ("სიახლეები", "#news"),
            ("კონტაქტი", "#contact"),
        ],

        "ui": {
            "about_label": "ჩემ შესახებ",
            "schedule": "კონსულტაციის დაჯავშნა",
            "download_cv": "CV-ის ჩამოტვირთვა",
            "expertise_title": "ექსპერტიზა",
            "expertise_sub": "სად იკვეთება ბიზნესი, ქონება და სამოქალაქო სამართალი "
                             "— და რას ვმართავ ყოველდღიურად.",
            "right_now": "მიმდინარე საქმიანობა",
            "highlights": "გამოცდილების მიმოხილვა",
            "contact_card": "კონტაქტი",
            "view_full": "სრული გამოცდილება",
            "experience_title": "გამოცდილება",
            "experience_sub": "შვიდწლიანი გამოცდილება ბანკებთან, დეველოპერებთან და "
                              "კერძო კლიენტებთან.",
            "education_title": "განათლება",
            "skills_title": "უნარები",
            "skills_panel": "იურიდიული ექსპერტიზა",
            "strengths_panel": "ძირითადი ძლიერი მხარეები",
            "languages_title": "ენები",
            "licenses_title": "ლიცენზიები და სერტიფიკატები",
            "hobbies_title": "ჰობი",
            "hobbies_sub": "ცხოვრება ოფისის მიღმა.",
            "news_title": "სიახლეები",
            "news_sub": "საქართველოს კანონმდებლობა, რომელიც კლიენტებს ყველაზე ხშირად ეხება.",
            "read_note": "სრულად ნახვა",
            "contact_title": "კონტაქტი",
            "get_in_touch": "დაკავშირება",
            "appointment": "კონსულტაცია წინასწარი შეთანხმებით, ორშაბათიდან "
                           "პარასკევამდე.",
            "form_title": "კონსულტაციის მოთხოვნა",
            "label_name": "თქვენი სახელი",
            "ph_name": "სახელი და გვარი",
            "label_email": "ელ. ფოსტა",
            "ph_email": "you@example.com",
            "label_message": "როგორ შემიძლია დაგეხმაროთ?",
            "ph_message": "მოკლედ აღწერეთ თქვენი საკითხი.",
            "send": "მოთხოვნის გაგზავნა",
            "rights": "ყველა უფლება დაცულია.",
            "menu": "მენიუს გახსნა",
            "theme": "ღია და მუქ რეჟიმს შორის გადართვა",
            "back_to_top": "დასაწყისში დაბრუნება",
            "listen": "მოსმენა",
            "stop_listening": "შეჩერება",
        },

        "speech": "მოგესალმებით. ეს არის გურამ მაღულარიას პირადი ვებგვერდი — "
                  "იურიდიული მრჩეველი შვიდწლიანი გამოცდილებით უძრავი ქონების "
                  "დეველოპმენტსა და საბანკო სამართალწარმოებაში. თუ სანდო "
                  "იურიდიულ გადაწყვეტებს ეძებთ, სწორ ადგილას ხართ.",

        "mail": {
            "subject": "კონსულტაციის მოთხოვნა",
            "label_name": "კლიენტის სახელი",
            "label_message": "როგორ შემიძლია დაგეხმაროთ?",
            "m_fill": "გთხოვთ, შეავსოთ: ",
            "f_name": "სახელი",
            "f_email": "ელ. ფოსტა",
            "f_message": "შეტყობინება",
            "m_bad_email": "ელ. ფოსტის მისამართი არასწორია.",
            "m_opening": "იხსნება თქვენი ფოსტის აპლიკაცია — გაგზავნეთ იქიდან.",
        },
    },
}

DEFAULT_LANG = "en"

# =========================================================
# 2. App
# =========================================================

FONT_AWESOME = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css"
GOOGLE_FONTS = (
    "https://fonts.googleapis.com/css2?"
    "family=Cormorant+Garamond:wght@400;500;600;700&"
    "family=Lato:wght@300;400;600;700;900&"
    "family=Noto+Sans+Georgian:wght@300;400;600;700&"
    "family=Noto+Serif+Georgian:wght@400;500;600;700&"
    "family=Great+Vibes&display=swap"
)

_EN = CONTENT["en"]
FULL_NAME_EN = f"{_EN['first_name']} {_EN['last_name']}"

app = Dash(
    __name__,
    title=f"{FULL_NAME_EN} — {_EN['role']}",
    update_title=None,
    external_stylesheets=[GOOGLE_FONTS, FONT_AWESOME],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"},
        {"name": "description",
         "content": f"{FULL_NAME_EN} — {_EN['role']}. "
                    f"{' | '.join(_EN['specialties'])}."},
    ],
)
server = app.server  # for gunicorn / deployment

# Applies the saved theme before first paint so there is no flash of light mode.
app.index_string = """<!DOCTYPE html>
<html lang="en" data-theme="light">
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <style>
            /* Hero backdrop: a wide band of the photo, faded out before the
               bottom of the section so the page still ends on clean cream. */
            .hero { isolation: isolate; }
            .hero__bg {
                position: absolute;
                inset: var(--header-h) 0 0 0;
                z-index: -1;
                background-size: cover;
                background-position: center 62%;
                background-repeat: no-repeat;
                opacity: .30;
                filter: grayscale(.35) contrast(.95);
                -webkit-mask-image: linear-gradient(180deg,
                    rgba(0,0,0,.95) 0%, rgba(0,0,0,.55) 45%, rgba(0,0,0,0) 92%);
                mask-image: linear-gradient(180deg,
                    rgba(0,0,0,.95) 0%, rgba(0,0,0,.55) 45%, rgba(0,0,0,0) 92%);
            }
            [data-theme="dark"] .hero__bg {
                opacity: .22;
                filter: grayscale(.5) brightness(.75);
            }
            @media (max-width: 900px) {
                .hero__bg { background-position: center 55%; opacity: .22; }
            }
            @media print { .hero__bg { display: none; } }
        </style>
        <script>
            (function () {
                try {
                    var saved = localStorage.getItem("gm-theme");
                    if (!saved) {
                        saved = window.matchMedia("(prefers-color-scheme: dark)").matches
                            ? "dark" : "light";
                    }
                    document.documentElement.setAttribute("data-theme", saved);
                } catch (e) {}
            })();
        </script>
    </head>
    <body>
        {%app_entry%}
        <footer>{%config%}{%scripts%}{%renderer%}</footer>
    </body>
</html>"""


# =========================================================
# 3. Building blocks
#    Every builder takes `c` — the content dict for the active language.
# =========================================================

def asset(filename: str) -> str:
    return app.get_asset_url(filename)


def full_name(c):
    return f"{c['first_name']} {c['last_name']}"


def specialties_line(c):
    """Renders the specialties line so a phrase never breaks across two lines."""
    parts = []
    for i, item in enumerate(c["specialties"]):
        if i:
            parts.append(html.Em("|"))
            parts.append(" ")  # the only place the line may break
        parts.append(html.Span(item))
    return parts


def section_head(title, subtitle=None):
    children = [html.H2(title), html.Div(className="rule")]
    if subtitle:
        children.append(html.P(subtitle))
    return html.Div(children, className="sec-head")


def timeline_item(job, show_tags=True, max_points=None):
    """One entry in a timeline. `max_points` trims the bullets for the summary card."""
    points = job["points"] if max_points is None else job["points"][:max_points]
    children = [
        html.P(job["role"], className="tl-role"),
        html.P(job["org"], className="tl-org"),
        html.P(job["date"], className="tl-date"),
        html.Ul([html.Li(p) for p in points], className="tl-desc"),
    ]
    if show_tags and job.get("tags"):
        children.append(
            html.Div(
                [html.Span(t, className="chip") for t in job["tags"]],
                className="tl-tags",
            )
        )
    return html.Div(children, className="tl-item")


def contact_row(icon, label, href=None, external=False):
    body = html.Span(label)
    if href:
        body = html.A(
            label,
            href=href,
            target="_blank" if external else None,
            rel="noopener noreferrer" if external else None,
        )
    return html.Div([html.I(className=icon), body], className="contact-row")


def contact_list(c):
    return html.Div(
        [
            contact_row("fa-regular fa-envelope", COMMON["email"],
                        f"mailto:{COMMON['email']}"),
            contact_row("fa-solid fa-phone", COMMON["phone"],
                        f"tel:{COMMON['phone_href']}"),
            contact_row("fa-solid fa-location-dot", c["location"]),
            contact_row("fa-brands fa-linkedin-in", COMMON["linkedin_label"],
                        COMMON["linkedin"], external=True),
        ],
        className="contact-list",
    )


def header(c):
    ui = c["ui"]
    return html.Header(
        html.Div(
            [
                html.A(
                    [
                        html.Div([html.Span("G"), html.Span("M")],
                                 className="brand__mark"),
                        html.Div(
                            [
                                html.Div(full_name(c), className="brand__name"),
                                html.Div(c["role"], className="brand__role"),
                            ]
                        ),
                    ],
                    href="#home",
                    className="brand",
                ),
                html.Nav(
                    [html.A(label, href=href) for label, href in c["nav"]],
                    id="primary-nav",
                    className="nav",
                ),
                html.Button(
                    html.I(className="fa-solid fa-volume-high", id="speak-icon"),
                    id="speak-btn",
                    className="icon-btn",
                    n_clicks=0,
                    title=ui["listen"],
                    **{"aria-label": ui["listen"]},
                ),
                dcc.Link(
                    c["switch_label"],
                    href=f"/?lang={c['switch_to']}",
                    className="icon-btn lang-btn",
                    title=c["switch_title"],
                ),
                html.Button(
                    html.I(className="fa-solid fa-moon", id="theme-icon"),
                    id="theme-toggle",
                    className="icon-btn",
                    n_clicks=0,
                    **{"aria-label": ui["theme"]},
                ),
                html.Button(
                    html.I(className="fa-solid fa-bars"),
                    id="nav-toggle",
                    className="icon-btn nav-toggle",
                    n_clicks=0,
                    **{"aria-label": ui["menu"], "aria-expanded": "false",
                       "aria-controls": "primary-nav"},
                ),
            ],
            className="wrap header__inner",
        ),
        className="header",
    )


def hero(c):
    ui = c["ui"]

    stats = html.Div(
        [
            html.Div(
                [
                    html.I(className=icon),
                    html.Div(
                        [
                            html.Div(
                                value,
                                className="stat__num"
                                if value[0].isdigit()
                                else "stat__num stat__num--text",
                            ),
                            html.Div(label, className="stat__label"),
                        ]
                    ),
                ],
                className="stat",
            )
            for icon, value, label in c["stats"]
        ],
        className="stats",
    )

    copy = html.Div(
        [
            html.Div(c["role"], className="eyebrow"),
            html.H1(
                [c["first_name"], html.Br(), c["last_name"]],
                className="hero__name",
            ),
            html.P(specialties_line(c), className="hero__specialties"),
            html.P(c["lede"], className="hero__lede"),
            html.Div(
                [
                    html.A(
                        [html.I(className="fa-regular fa-calendar-check"),
                         ui["schedule"]],
                        href="#contact",
                        className="btn btn--solid",
                    ),
                    html.A(
                        [html.I(className="fa-solid fa-download"), ui["download_cv"]],
                        href=asset(COMMON["cv_file"]),
                        className="btn btn--ghost",
                        download=COMMON["cv_file"],
                    ),
                ],
                className="hero__actions",
            ),
            stats,
        ],
        className="hero__copy",
    )

    about_card = html.Div(
        [
            html.Div(
                [
                    html.Span(ui["about_label"], className="habout__label"),
                    html.Span([html.Span("G"), html.Span("M")],
                              className="habout__mark"),
                ],
                className="habout__top",
            ),
            html.P(c["about_lead"], className="habout__lead"),
            html.P(c["about"], className="habout__body"),
            html.Div(
                [
                    html.Div(
                        [
                            html.Span(label, className="fact__label"),
                            html.Span(value, className="fact__value"),
                        ],
                        className="fact",
                    )
                    for label, value in c["hero_facts"]
                ],
                className="facts",
            ),
        ],
        className="habout",
    )

    return html.Section(
        [
            html.Div(
                className="hero__bg",
                style={"backgroundImage": f"url('{asset(COMMON['hero_bg'])}')"},
            ),
            html.Div(
                html.Div([copy, about_card], className="hero__grid"),
                className="wrap",
            ),
        ],
        id="home",
        className="hero",
    )


def expertise(c):
    ui = c["ui"]
    return html.Section(
        html.Div(
            [
                section_head(ui["expertise_title"], ui["expertise_sub"]),
                html.Div(
                    [
                        html.Article(
                            [html.I(className=icon), html.H3(title), html.P(desc)],
                            className="card reveal",
                        )
                        for icon, title, desc in c["expertise"]
                    ],
                    className="cards",
                ),
            ],
            className="wrap",
        ),
        id="practice",
        className="section section--alt",
    )


def about_band(c):
    ui = c["ui"]

    focus_col = html.Div(
        [
            html.H3(ui["right_now"]),
            html.Div(className="rule"),
            html.Ul([html.Li(item) for item in c["focus_now"]], className="focus"),
            html.Div(full_name(c), className="signature"),
        ],
        className="band__col",
    )

    highlights_col = html.Div(
        [
            html.H3(ui["highlights"]),
            html.Div(className="rule"),
            html.Div(
                [timeline_item(job, show_tags=False, max_points=2)
                 for job in c["experience"][:2]],
                className="timeline",
            ),
            html.A(ui["view_full"], href="#experience",
                   className="btn btn--solid btn--sm", style={"marginTop": "24px"}),
        ],
        className="band__col",
    )

    contact_col = html.Div(
        [
            html.H3(ui["contact_card"]),
            html.Div(className="rule"),
            contact_list(c),
        ],
        className="band__col band__col--contact",
    )

    return html.Section(
        html.Div(
            html.Div([focus_col, highlights_col, contact_col],
                     className="band reveal"),
            className="wrap",
        ),
        id="about",
        className="section section--tight",
    )


def experience(c):
    ui = c["ui"]
    return html.Section(
        html.Div(
            [
                section_head(ui["experience_title"], ui["experience_sub"]),
                html.Div(
                    html.Div(
                        [timeline_item(job) for job in c["experience"]],
                        className="timeline",
                    ),
                    className="panel reveal",
                ),
            ],
            className="wrap",
        ),
        id="experience",
        className="section section--alt",
    )


def education(c):
    return html.Section(
        html.Div(
            [
                section_head(c["ui"]["education_title"]),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(html.I(className="fa-solid fa-graduation-cap"),
                                         className="edu__icon"),
                                html.Div(
                                    [
                                        html.H4(item["degree"]),
                                        html.Span(item["school"]),
                                        html.P(item["date"], className="tl-date"),
                                        html.Span(item["note"]),
                                    ]
                                ),
                            ],
                            className="edu",
                        )
                        for item in c["education"]
                    ],
                    className="panel reveal",
                ),
            ],
            className="wrap",
        ),
        id="education",
        className="section",
    )


def skills(c):
    ui = c["ui"]

    bars = html.Div(
        [
            html.H3(ui["skills_panel"]),
            *[
                html.Div(
                    [
                        html.Div(
                            [html.Span(name), html.Span(label)],
                            className="skill__top",
                        ),
                        html.Div(html.I(style={"width": f"{fill}%"}), className="bar"),
                    ],
                    className="skill",
                )
                for name, label, fill in c["skills"]
            ],
        ],
        className="panel reveal",
    )

    tags = html.Div(
        [
            html.H3(ui["strengths_panel"]),
            html.Div(
                [html.Span(s, className="chip") for s in c["soft_skills"]],
                className="tl-tags",
            ),
        ],
        className="panel reveal",
    )

    return html.Section(
        html.Div(
            [section_head(ui["skills_title"]),
             html.Div([bars, tags], className="grid-2")],
            className="wrap",
        ),
        id="skills",
        className="section section--alt",
    )


def languages(c):
    return html.Section(
        html.Div(
            [
                section_head(c["ui"]["languages_title"]),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    html.B(f"{pct}%"),
                                    className="lang__ring",
                                    style={
                                        "background": (
                                            "conic-gradient(var(--gold) "
                                            f"{pct}%, var(--border) 0)"
                                        )
                                    },
                                ),
                                html.H4(name),
                                html.Span(level),
                            ],
                            className="panel lang reveal",
                        )
                        for name, level, pct in c["languages"]
                    ],
                    className="grid-3",
                ),
            ],
            className="wrap",
        ),
        id="languages",
        className="section",
    )


def licenses(c):
    return html.Section(
        html.Div(
            [
                section_head(c["ui"]["licenses_title"]),
                html.Div(
                    [
                        html.Div(
                            [
                                html.I(className=icon),
                                html.Div([html.H4(title), html.Span(desc)]),
                            ],
                            className="panel licence reveal",
                        )
                        for icon, title, desc in c["licenses"]
                    ],
                    className="grid-2",
                ),
            ],
            className="wrap",
        ),
        id="licenses",
        className="section section--alt",
    )


def hobbies(c):
    ui = c["ui"]
    return html.Section(
        html.Div(
            [
                section_head(ui["hobbies_title"], ui["hobbies_sub"]),
                html.Div(
                    [
                        html.Div(
                            [html.I(className=icon), html.H4(title), html.Span(desc)],
                            className="panel hobby reveal",
                        )
                        for icon, title, desc in c["hobbies"]
                    ],
                    className="grid-3",
                ),
            ],
            className="wrap",
        ),
        id="hobbies",
        className="section",
    )


def news(c):
    ui = c["ui"]
    return html.Section(
        html.Div(
            [
                section_head(ui["news_title"], ui["news_sub"]),
                html.Div(
                    [
                        html.Article(
                            [
                                html.Div(item["date"], className="eyebrow"),
                                html.H4(item["title"]),
                                html.P(item["excerpt"]) if item.get("excerpt")
                                else None,
                                html.A(
                                    [ui["read_note"],
                                     html.I(className="fa-solid fa-arrow-right")],
                                    href=item["url"],
                                    className="more",
                                    target="_blank",
                                    rel="noopener noreferrer",
                                ),
                            ],
                            className="news-card reveal",
                        )
                        for item in c["news"]
                    ],
                    className="grid-3",
                ),
            ],
            className="wrap",
        ),
        id="news",
        className="section section--alt",
    )


def contact(c):
    ui = c["ui"]

    details = html.Div(
        [
            html.Div(
                [
                    html.Img(src=asset(COMMON["photo"]),
                             alt=full_name(c), className="contact-avatar"),
                    html.H3(ui["get_in_touch"]),
                ],
                className="contact-head",
            ),
            html.Div(className="rule"),
            contact_list(c),
            html.Div(
                [
                    html.A(html.I(className="fa-brands fa-linkedin-in"),
                           href=COMMON["linkedin"], target="_blank",
                           rel="noopener noreferrer",
                           **{"aria-label": "LinkedIn"}),
                    html.A(html.I(className="fa-regular fa-envelope"),
                           href=f"mailto:{COMMON['email']}",
                           **{"aria-label": "Email"}),
                    html.A(html.I(className="fa-solid fa-phone"),
                           href=f"tel:{COMMON['phone_href']}",
                           **{"aria-label": "Phone"}),
                ],
                className="socials",
            ),
            html.P(ui["appointment"], className="map-note"),
        ],
        className="band__col band__col--contact",
        style={"borderRadius": "4px"},
    )

    form = html.Div(
        [
            html.H3(ui["form_title"]),
            html.Div(
                [
                    html.Label(ui["label_name"], htmlFor="in-name"),
                    dcc.Input(id="in-name", type="text", placeholder=ui["ph_name"],
                              debounce=True),
                ],
                className="field",
            ),
            html.Div(
                [
                    html.Label(ui["label_email"], htmlFor="in-email"),
                    dcc.Input(id="in-email", type="email", placeholder=ui["ph_email"],
                              debounce=True),
                ],
                className="field",
            ),
            html.Div(
                [
                    html.Label(ui["label_message"], htmlFor="in-message"),
                    dcc.Textarea(id="in-message", placeholder=ui["ph_message"]),
                ],
                className="field",
            ),
            html.Button(ui["send"], id="send-btn", className="btn btn--solid",
                        n_clicks=0),
            html.Div(id="form-status", className="form-status", role="status"),
        ],
        className="panel",
    )

    return html.Section(
        html.Div(
            [
                section_head(ui["contact_title"]),
                html.Div([details, form], className="contact-grid reveal"),
            ],
            className="wrap",
        ),
        id="contact",
        className="section",
    )


def footer(c):
    ui = c["ui"]
    labels = [label for label, _ in c["nav"]]
    return html.Footer(
        html.Div(
            [
                html.Div(f"© 2026 {full_name(c)}. {ui['rights']}"),
                html.Div(
                    [
                        html.A(labels[1], href="#practice"),
                        " · ",
                        html.A(labels[2], href="#experience"),
                        " · ",
                        html.A(labels[-1], href="#contact"),
                    ]
                ),
            ],
            className="wrap footer__inner",
        ),
        className="footer",
    )


# =========================================================
# 4. Layout
# =========================================================

def build_page(lang):
    """Assembles the whole page in one language."""
    c = CONTENT.get(lang, CONTENT[DEFAULT_LANG])
    return [
        header(c),
        html.Main(
            [
                hero(c),
                expertise(c),
                about_band(c),
                experience(c),
                education(c),
                skills(c),
                languages(c),
                licenses(c),
                hobbies(c),
                news(c),
                contact(c),
            ]
        ),
        footer(c),
        html.Button(html.I(className="fa-solid fa-arrow-up"), id="to-top",
                    className="to-top", n_clicks=0,
                    **{"aria-label": c["ui"]["back_to_top"]}),
        # Everything the browser-side code needs: the mail strings, plus the
        # page language and title so they can follow the switch.
        dcc.Store(
            id="mail-config",
            data={
                "email": COMMON["email"],
                "lang": c["html_lang"],
                "title": f"{full_name(c)} — {c['role']}",
                "speech": c["speech"],
                **c["mail"],
            },
        ),
    ]


app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        html.Div(build_page(DEFAULT_LANG), id="page"),
    ]
)


# =========================================================
# 5. Callbacks
# =========================================================

@app.callback(Output("page", "children"), Input("url", "search"))
def switch_language(search):
    """Rebuilds the whole page whenever ?lang= changes."""
    lang = DEFAULT_LANG
    if search and "lang=" in search:
        lang = search.split("lang=")[1].split("&")[0]
    return build_page(lang if lang in CONTENT else DEFAULT_LANG)


# Keeps <html lang> and the browser tab title in step with the language.
app.clientside_callback(
    ClientsideFunction(namespace="gm", function_name="applyLang"),
    Output("mail-config", "modified_timestamp"),
    Input("mail-config", "data"),
)

# Dark / light mode — remembers the choice in the browser.
app.clientside_callback(
    ClientsideFunction(namespace="gm", function_name="toggleTheme"),
    Output("theme-icon", "className"),
    Input("theme-toggle", "n_clicks"),
)

# Reads the spoken welcome using the browser's own speech synthesis.
app.clientside_callback(
    ClientsideFunction(namespace="gm", function_name="speakAbout"),
    Output("speak-icon", "className"),
    Input("speak-btn", "n_clicks"),
    State("mail-config", "data"),
)

# Consultation form — opens the visitor's own mail app with the request
# pre-written. Nothing is sent until they press send there.
app.clientside_callback(
    ClientsideFunction(namespace="gm", function_name="mailtoRequest"),
    Output("form-status", "children"),
    Output("form-status", "className"),
    Input("send-btn", "n_clicks"),
    State("mail-config", "data"),
    State("in-name", "value"),
    State("in-email", "value"),
    State("in-message", "value"),
    prevent_initial_call=True,
)


if __name__ == "__main__":
    app.run(debug=True)
