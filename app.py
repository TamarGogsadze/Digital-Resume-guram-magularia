"""
Guram Magularia — Legal Counsel
Digital resume / personal website built with Dash.

Run:
    pip install -r requirements.txt
    python app.py
    → http://127.0.0.1:8050

Everything you need to edit lives in the CONTENT block below.
Layout and styling live in assets/styles.css and assets/site.js.
"""

from dash import Dash, dcc, html, Input, Output, State, callback, no_update

# =========================================================
# 1. CONTENT — edit everything here
# =========================================================

PROFILE = {
    "first_name": "Guram",
    "last_name": "Magularia",
    "role": "Legal Counsel",
    "specialties": ["Civil & Legal Law", "Contract & Business Law", "Real Estate Law"],
    "lede": "Providing strategic legal solutions with precision, integrity, "
            "and a commitment to your success.",
    "quote": "My mission is to deliver practical legal solutions and protect "
             "what matters most to my clients.",
    "about": "Highly experienced Legal Counsel with expertise in civil law, contract law, "
             "business law, and real estate law. Proven ability to handle complex legal "
             "matters, negotiate high-value agreements, and ensure regulatory compliance. "
             "Skilled in leading legal teams, advising top-tier real estate developers, and "
             "mitigating legal risks in dynamic business environments.",
    "photo": "profile.PNG",               # file inside /assets
    "cv_file": "Guram_Magularia_CV.pdf",  # drop your PDF into /assets
    "email": "guram.magularia@email.com",
    "phone": "+995 555 12 34 56",
    "phone_href": "+995555123456",
    "location": "Tbilisi, Georgia",
    "linkedin": "https://www.linkedin.com/in/gurammagularia",
    "linkedin_label": "linkedin.com/in/gurammagularia",
}

# (icon, headline value, supporting label)
STATS = [
    ("fa-solid fa-briefcase", "7+", "Years of Experience"),
    ("fa-solid fa-gavel", "100+", "Cases Handled"),
    ("fa-solid fa-users", "Corporate &", "Individual Clients"),
    ("fa-solid fa-shield-halved", "Strong Legal", "Solutions"),
]

PRACTICE_AREAS = [
    ("fa-solid fa-landmark", "Civil Law",
     "Representation in civil disputes and litigation."),
    ("fa-solid fa-file-signature", "Contract Law",
     "Drafting, reviewing, and negotiating contracts."),
    ("fa-solid fa-briefcase", "Business Law",
     "Legal support for business operations and compliance."),
    ("fa-solid fa-house-chimney", "Real Estate Law",
     "Real estate transactions, leases, and property disputes."),
    ("fa-solid fa-users-rectangle", "Corporate Law",
     "Corporate structuring, governance and legal advisory."),
    ("fa-solid fa-scale-balanced", "Dispute Resolution",
     "Effective representation in negotiation and litigation."),
]

EXPERIENCE = [
    {
        "role": "Head of Legal Department",
        "org": "NEXT — Real Estate Developer Company",
        "date": "2021 – Present",
        "points": [
            "Led the legal department of a top real estate development company, "
            "providing expert guidance on contractual, regulatory, and dispute "
            "resolution matters.",
            "Negotiated and drafted high-value contracts, ensuring compliance with "
            "Georgian and international legal standards.",
            "Managed litigation and dispute resolution processes, minimizing company "
            "risks and financial exposure.",
            "Advised executive leadership on legal strategies, compliance, and "
            "business expansion initiatives.",
            "Successfully handled legal due diligence for multi-million-dollar real "
            "estate transactions.",
        ],
        "tags": ["Real Estate", "Contracts", "Due Diligence", "Team Leadership"],
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
            "Represented the bank in court proceedings and before administrative bodies.",
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
]

EDUCATION = [
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
]

SKILLS = [
    ("Contract Drafting & Negotiation", 95),
    ("Civil & Commercial Litigation", 90),
    ("Real Estate Transactions", 92),
    ("Corporate Governance", 85),
    ("Regulatory Compliance", 88),
]

SOFT_SKILLS = [
    "Legal Research", "Risk Assessment", "Client Advisory", "Due Diligence",
    "Mediation", "Team Leadership", "Legal Writing", "Case Strategy",
]

LANGUAGES = [
    ("Georgian", "Native", 100),
    ("English", "Professional — C1", 85),
    ("Russian", "Advanced — B2/C1", 80),
]

LICENSES = [
    ("fa-solid fa-certificate", "Bar Admission — Georgia",
     "Licensed to practise law, Georgian Bar Association."),
    ("fa-solid fa-award", "Certified Mediator",
     "Accredited in commercial and civil mediation."),
    ("fa-solid fa-book-open", "Real Estate Law Certification",
     "Advanced programme in property and development law."),
    ("fa-solid fa-shield-halved", "Corporate Compliance Training",
     "Regulatory compliance and anti-corruption standards."),
]

NEWS = [
    {
        "date": "May 2026",
        "title": "New rules for property registration",
        "excerpt": "What the latest amendments mean for developers and buyers "
                   "closing deals this year.",
        "url": "#",
    },
    {
        "date": "March 2026",
        "title": "Drafting lease agreements that hold up",
        "excerpt": "Five clauses that decide most commercial lease disputes — "
                   "and how to write them.",
        "url": "#",
    },
    {
        "date": "January 2026",
        "title": "Speaking at the Tbilisi Business Law Forum",
        "excerpt": "A panel on contract risk in cross-border real estate "
                   "development projects.",
        "url": "#",
    },
]

NAV_LINKS = [
    ("Home", "#home"),
    ("Practice Areas", "#practice"),
    ("Experience", "#experience"),
    ("Education", "#education"),
    ("Skills", "#skills"),
    ("Languages", "#languages"),
    ("Licenses", "#licenses"),
    ("News", "#news"),
    ("Contact", "#contact"),
]

FULL_NAME = f"{PROFILE['first_name']} {PROFILE['last_name']}"

# =========================================================
# 2. App
# =========================================================

FONT_AWESOME = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css"
GOOGLE_FONTS = (
    "https://fonts.googleapis.com/css2?"
    "family=Cormorant+Garamond:wght@400;500;600;700&"
    "family=Lato:wght@300;400;600;700;900&"
    "family=Great+Vibes&display=swap"
)

app = Dash(
    __name__,
    title=f"{FULL_NAME} — {PROFILE['role']}",
    update_title=None,
    external_stylesheets=[GOOGLE_FONTS, FONT_AWESOME],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"},
        {"name": "description",
         "content": f"{FULL_NAME} — {PROFILE['role']}. "
                    f"{' | '.join(PROFILE['specialties'])}."},
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
# =========================================================

def asset(filename: str) -> str:
    return app.get_asset_url(filename)


def specialties_line():
    """Renders the practice line so a phrase never breaks across two lines."""
    parts = []
    for i, item in enumerate(PROFILE["specialties"]):
        if i:
            parts.append(html.Em("|"))
            parts.append(" ")  # the only place the line may break
        parts.append(html.Span(item))
    return parts


def section_head(title, subtitle=None, align="center"):
    cls = "sec-head" if align == "center" else "sec-head sec-head--left"
    children = [html.H2(title), html.Div(className="rule")]
    if subtitle:
        children.append(html.P(subtitle))
    return html.Div(children, className=cls)


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


def header():
    return html.Header(
        html.Div(
            [
                html.A(
                    [
                        html.Div([html.Span("G"), html.Span("M")], className="brand__mark"),
                        html.Div(
                            [
                                html.Div(FULL_NAME, className="brand__name"),
                                html.Div(PROFILE["role"], className="brand__role"),
                            ]
                        ),
                    ],
                    href="#home",
                    className="brand",
                    **{"aria-label": f"{FULL_NAME}, back to top"},
                ),
                html.Nav(
                    [html.A(label, href=href) for label, href in NAV_LINKS],
                    id="primary-nav",
                    className="nav",
                ),
                html.Button(
                    html.I(className="fa-solid fa-moon", id="theme-icon"),
                    id="theme-toggle",
                    className="icon-btn",
                    n_clicks=0,
                    **{"aria-label": "Switch between light and dark mode"},
                ),
                html.Button(
                    html.I(className="fa-solid fa-bars"),
                    id="nav-toggle",
                    className="icon-btn nav-toggle",
                    n_clicks=0,
                    **{"aria-label": "Open menu", "aria-expanded": "false",
                       "aria-controls": "primary-nav"},
                ),
            ],
            className="wrap header__inner",
        ),
        className="header",
    )


def hero():
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
            for icon, value, label in STATS
        ],
        className="stats",
    )

    copy = html.Div(
        [
            html.Div(PROFILE["role"], className="eyebrow"),
            html.H1(
                [PROFILE["first_name"], html.Br(), PROFILE["last_name"]],
                className="hero__name",
            ),
            html.P(specialties_line(), className="hero__specialties"),
            html.P(PROFILE["lede"], className="hero__lede"),
            html.Div(
                [
                    html.A(
                        [html.I(className="fa-regular fa-calendar-check"),
                         "Schedule consultation"],
                        href="#contact",
                        className="btn btn--solid",
                    ),
                    html.A(
                        [html.I(className="fa-solid fa-download"), "Download CV"],
                        href=asset(PROFILE["cv_file"]),
                        className="btn btn--ghost",
                        download=PROFILE["cv_file"],
                    ),
                ],
                className="hero__actions",
            ),
            stats,
        ],
        className="hero__copy",
    )

    visual = html.Div(
        [
            html.Div(className="hero__arc"),
            html.Div(
                html.Img(src=asset(PROFILE["photo"]), alt=f"Portrait of {FULL_NAME}"),
                className="hero__photo",
            ),
            html.Blockquote(
                [
                    html.I(className="fa-solid fa-quote-left"),
                    html.P(PROFILE["quote"]),
                ],
                className="quote",
            ),
        ],
        className="hero__visual",
    )

    return html.Section(
        [html.Div(copy, className="wrap"), visual],
        id="home",
        className="hero",
    )


def practice_areas():
    return html.Section(
        html.Div(
            [
                section_head(
                    "Practice Areas",
                    "Focused legal support across the areas where business, "
                    "property and civil law meet.",
                ),
                html.Div(
                    [
                        html.Article(
                            [
                                html.I(className=icon),
                                html.H3(title),
                                html.P(desc),
                            ],
                            className="card reveal",
                        )
                        for icon, title, desc in PRACTICE_AREAS
                    ],
                    className="cards",
                ),
            ],
            className="wrap",
        ),
        id="practice",
        className="section section--alt",
    )


def about_band():
    about_col = html.Div(
        [
            html.H3("About me"),
            html.Div(className="rule"),
            html.P(PROFILE["about"]),
            html.Div(FULL_NAME, className="signature"),
        ],
        className="band__col",
    )

    highlights_col = html.Div(
        [
            html.H3("Experience highlights"),
            html.Div(className="rule"),
            html.Div(
                [timeline_item(job, show_tags=False, max_points=2)
                 for job in EXPERIENCE[:2]],
                className="timeline",
            ),
            html.A("View full experience", href="#experience",
                   className="btn btn--solid btn--sm", style={"marginTop": "24px"}),
        ],
        className="band__col",
    )

    contact_col = html.Div(
        [
            html.H3("Contact"),
            html.Div(className="rule"),
            html.Div(
                [
                    contact_row("fa-regular fa-envelope", PROFILE["email"],
                                f"mailto:{PROFILE['email']}"),
                    contact_row("fa-solid fa-phone", PROFILE["phone"],
                                f"tel:{PROFILE['phone_href']}"),
                    contact_row("fa-solid fa-location-dot", PROFILE["location"]),
                    contact_row("fa-brands fa-linkedin-in", PROFILE["linkedin_label"],
                                PROFILE["linkedin"], external=True),
                ],
                className="contact-list",
            ),
        ],
        className="band__col band__col--contact",
    )

    return html.Section(
        html.Div(
            html.Div([about_col, highlights_col, contact_col], className="band reveal"),
            className="wrap",
        ),
        id="about",
        className="section section--tight",
    )


def experience():
    return html.Section(
        html.Div(
            [
                section_head("Experience",
                             "Seven years advising banks, developers and "
                             "private clients."),
                html.Div(
                    html.Div(
                        [timeline_item(job) for job in EXPERIENCE],
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


def education():
    return html.Section(
        html.Div(
            [
                section_head("Education"),
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
                        for item in EDUCATION
                    ],
                    className="panel reveal",
                ),
            ],
            className="wrap",
        ),
        id="education",
        className="section",
    )


def skills():
    bars = html.Div(
        [
            html.H3("Legal expertise"),
            *[
                html.Div(
                    [
                        html.Div(
                            [html.Span(name), html.Span(f"{level}%")],
                            className="skill__top",
                        ),
                        html.Div(
                            html.I(style={"width": f"{level}%"}),
                            className="bar",
                        ),
                    ],
                    className="skill",
                )
                for name, level in SKILLS
            ],
        ],
        className="panel reveal",
    )

    tags = html.Div(
        [
            html.H3("Core strengths"),
            html.Div(
                [html.Span(s, className="chip") for s in SOFT_SKILLS],
                className="tl-tags",
            ),
        ],
        className="panel reveal",
    )

    return html.Section(
        html.Div(
            [section_head("Skills"), html.Div([bars, tags], className="grid-2")],
            className="wrap",
        ),
        id="skills",
        className="section section--alt",
    )


def languages():
    return html.Section(
        html.Div(
            [
                section_head("Languages"),
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
                        for name, level, pct in LANGUAGES
                    ],
                    className="grid-3",
                ),
            ],
            className="wrap",
        ),
        id="languages",
        className="section",
    )


def licenses():
    return html.Section(
        html.Div(
            [
                section_head("Licenses & Certifications"),
                html.Div(
                    [
                        html.Div(
                            [
                                html.I(className=icon),
                                html.Div([html.H4(title), html.Span(desc)]),
                            ],
                            className="panel licence reveal",
                        )
                        for icon, title, desc in LICENSES
                    ],
                    className="grid-2",
                ),
            ],
            className="wrap",
        ),
        id="licenses",
        className="section section--alt",
    )


def news():
    return html.Section(
        html.Div(
            [
                section_head("News & Insights",
                             "Notes on legal developments that affect clients "
                             "in Georgia."),
                html.Div(
                    [
                        html.Article(
                            [
                                html.Div(item["date"], className="eyebrow"),
                                html.H4(item["title"]),
                                html.P(item["excerpt"]),
                                html.A(
                                    ["Read the note",
                                     html.I(className="fa-solid fa-arrow-right")],
                                    href=item["url"],
                                    className="more",
                                ),
                            ],
                            className="news-card reveal",
                        )
                        for item in NEWS
                    ],
                    className="grid-3",
                ),
            ],
            className="wrap",
        ),
        id="news",
        className="section",
    )


def contact():
    details = html.Div(
        [
            html.H3("Get in touch"),
            html.Div(className="rule"),
            html.Div(
                [
                    contact_row("fa-regular fa-envelope", PROFILE["email"],
                                f"mailto:{PROFILE['email']}"),
                    contact_row("fa-solid fa-phone", PROFILE["phone"],
                                f"tel:{PROFILE['phone_href']}"),
                    contact_row("fa-solid fa-location-dot", PROFILE["location"]),
                    contact_row("fa-brands fa-linkedin-in", PROFILE["linkedin_label"],
                                PROFILE["linkedin"], external=True),
                ],
                className="contact-list",
            ),
            html.Div(
                [
                    html.A(html.I(className="fa-brands fa-linkedin-in"),
                           href=PROFILE["linkedin"], target="_blank",
                           rel="noopener noreferrer",
                           **{"aria-label": "LinkedIn"}),
                    html.A(html.I(className="fa-regular fa-envelope"),
                           href=f"mailto:{PROFILE['email']}",
                           **{"aria-label": "Email"}),
                    html.A(html.I(className="fa-solid fa-phone"),
                           href=f"tel:{PROFILE['phone_href']}",
                           **{"aria-label": "Phone"}),
                ],
                className="socials",
            ),
            html.P("Consultations by appointment, Monday to Friday.",
                   className="map-note"),
        ],
        className="band__col band__col--contact",
        style={"borderRadius": "4px"},
    )

    form = html.Div(
        [
            html.H3("Request a consultation"),
            html.Div(
                [
                    html.Label("Your name", htmlFor="in-name"),
                    dcc.Input(id="in-name", type="text", placeholder="Full name",
                              debounce=True),
                ],
                className="field",
            ),
            html.Div(
                [
                    html.Label("Email", htmlFor="in-email"),
                    dcc.Input(id="in-email", type="email", placeholder="you@example.com",
                              debounce=True),
                ],
                className="field",
            ),
            html.Div(
                [
                    html.Label("How can I help?", htmlFor="in-message"),
                    dcc.Textarea(id="in-message",
                                 placeholder="A short description of your matter."),
                ],
                className="field",
            ),
            html.Button("Send request", id="send-btn", className="btn btn--solid",
                        n_clicks=0),
            html.Div(id="form-status", className="form-status", role="status"),
        ],
        className="panel",
    )

    return html.Section(
        html.Div(
            [
                section_head("Contact"),
                html.Div([details, form], className="contact-grid reveal"),
            ],
            className="wrap",
        ),
        id="contact",
        className="section section--alt",
    )


def footer():
    return html.Footer(
        html.Div(
            [
                html.Div(f"© 2026 {FULL_NAME}. All rights reserved."),
                html.Div(
                    [
                        html.A("Practice areas", href="#practice"),
                        " · ",
                        html.A("Experience", href="#experience"),
                        " · ",
                        html.A("Contact", href="#contact"),
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

app.layout = html.Div(
    [
        header(),
        html.Main(
            [
                hero(),
                practice_areas(),
                about_band(),
                experience(),
                education(),
                skills(),
                languages(),
                licenses(),
                news(),
                contact(),
            ]
        ),
        footer(),
        html.Button(html.I(className="fa-solid fa-arrow-up"), id="to-top",
                    className="to-top", n_clicks=0,
                    **{"aria-label": "Back to top"}),
    ]
)


# =========================================================
# 5. Callbacks
# =========================================================

# Dark / light mode — runs in the browser, remembers the choice.
app.clientside_callback(
    """
    function (n) {
        var root = document.documentElement;
        var current = root.getAttribute("data-theme") || "light";
        var next = current === "dark" ? "light" : "dark";
        if (n) {
            root.setAttribute("data-theme", next);
            try { localStorage.setItem("gm-theme", next); } catch (e) {}
            current = next;
        }
        return current === "dark"
            ? "fa-solid fa-sun"
            : "fa-solid fa-moon";
    }
    """,
    Output("theme-icon", "className"),
    Input("theme-toggle", "n_clicks"),
)


@callback(
    Output("form-status", "children"),
    Output("form-status", "className"),
    Input("send-btn", "n_clicks"),
    State("in-name", "value"),
    State("in-email", "value"),
    State("in-message", "value"),
    prevent_initial_call=True,
)
def submit_request(n_clicks, name, email, message):
    """Validates the consultation form.

    Replace the success branch with your own delivery step — Web3Forms,
    SMTP, or writing the request to a database.
    """
    if not n_clicks:
        return no_update, no_update

    missing = [
        label
        for label, value in (("name", name), ("email", email), ("message", message))
        if not (value or "").strip()
    ]
    if missing:
        return f"Please add your {', '.join(missing)}.", "form-status err"

    if "@" not in email or "." not in email.split("@")[-1]:
        return "That email address doesn't look right.", "form-status err"

    # TODO: send the message here.
    return (
        f"Thank you, {name.split()[0]}. Your request has been received — "
        f"you will get a reply at {email} within one business day.",
        "form-status ok",
    )

server=app.server
if __name__ == "__main__":
    app.run(debug=True)
