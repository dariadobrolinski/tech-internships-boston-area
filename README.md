# Boston Area Tech Internship Finder

An automated script to search and aggregate tech internship opportunities in the Boston area (and remote) from multiple sources including Greenhouse, Lever, Adzuna, and community-maintained GitHub job boards (SimplifyJobs, speedyapply, vanshb03).

I know this isn't perfect so if there are any issues feel free to contribute!

📖 **Documentation**
- [Setup Instructions](#setup-instructions)
- [Data Sources](#data-sources) - Where job listings come from
- [API Keys Guide](docs/API_KEYS.md) - How to get Adzuna & SERP API keys
- [Contributing Guide](docs/CONTRIBUTING.md) - How to contribute to this project

---

## Job Listings

| Company Name | Job Title | Location | Date Posted | APPLY |
|---|---|---|---|:-:|
| Sanofi | Agentic AI for CMC Digitalization | Framingham, MA | 10/23/2025 | [APPLY](https://sanofi.wd3.myworkdayjobs.com/en-US/SanofiCareers/job/Framingham-MA/Summer-2026-Intern---Agentic-AI-for-CMC-Digitalization_R2816447?utm_source=Simplify&ref=Simplify) |
| Second Dinner | 2026 AI/ML Engineer Intern | Remote in USA | 10/23/2025 | [APPLY](https://jobs.ashbyhq.com/SecondDinner/16e290f9-d116-4a81-b6f4-ff453722eb38/application?utm_source=Simplify&ref=Simplify) |
| Experian | Data Analyst Intern | Remote in USA | 10/22/2025 | [APPLY](https://jobs.smartrecruiters.com/Experian/744000089133739?utm_source=github-vansh-ouckah) |
| Clerkie | Software Engineer Intern | Remote in USA | 10/22/2025 | [APPLY](https://www.getfiber.ai/careers?gh_jid=4949164007&utm_source=github-vansh-ouckah) |
| Experian | Full Stack SWE Summer Intern - Remote & Paid | Remote in USA | 10/22/2025 | [APPLY](https://jobs.smartrecruiters.com/Experian/744000089140956?utm_source=Simplify&ref=Simplify) |
| Second Dinner | 2026 Product Manager Intern - Unannounced Super Fun Video Game | Remote in USA | 10/22/2025 | [APPLY](https://jobs.ashbyhq.com/SecondDinner/15d9eea6-8ab6-486d-84ac-9de05be54901/application?utm_source=Simplify&ref=Simplify) |
| Microsoft | Research Intern - Machine Learning for Biology and Healthcare | Cambridge, MA | 10/22/2025 | [APPLY](https://jobs.careers.microsoft.com/global/en/job/1900590?utm_source=Simplify&ref=Simplify) |
| J.M. Smucker | Data Science Intern - Masters or PhD - Summer 2026 | Remote in USA | 10/22/2025 | [APPLY](https://smucker.wd5.myworkdayjobs.com/US_External_Careers/job/Working-Remote-USA/Data-Science-Intern--Masters-or-PhD---Summer-2026_114447?utm_source=Simplify&ref=Simplify) |
| Microsoft | Research Intern, Machine Learning and Statistics | Cambridge, MA | 10/21/2025 | [APPLY](https://jobs.careers.microsoft.com/global/en/job/1900003?utm_source=github-vansh-ouckah) |
| Clerkie | Software Engineer Internship | Remote in USA | 10/21/2025 | [APPLY](https://www.getfiber.ai/careers?gh_jid=4949164007&utm_source=Simplify&ref=Simplify) |
| Pega | Software Engineer Summer Intern, Software Delivery Excellence Alliance | Waltham, MA | 10/21/2025 | [APPLY](https://www.pega.com/about/careers/22692/software-engineer-summer-intern-software-delivery-excellence-alliance?utm_source=Simplify&ref=Simplify) |
| Zipcar | Member Services Co-Op-Knowledge and Quality Enablement | Boston, MA | 10/19/2025 | [APPLY](https://avisbudget.wd1.myworkdayjobs.com/Zipcar_Careers/job/35-Thomson-Pl-Boston-02210/Member-Services-Co-Op--Knowledge-and-Quality-Enablement_R0181487?utm_source=Simplify&ref=Simplify) |
| Clerkie | Software Engineer Internship - 4 openings | Remote | 10/18/2025 | [APPLY](https://www.clerkie.io) |
| Pega | Software Engineer Intern | Waltham, MA | 10/18/2025 | [APPLY](https://www.pega.com/about/careers/22692/software-engineer-summer-intern-software-delivery-excellence-alliance?utm_source=github-vansh-ouckah) |
| Toast | MBA Product Manager Intern | Boston, MA | 10/18/2025 | [APPLY](https://boards.greenhouse.io/embed/job_app?token=7254875&utm_source=Simplify&ref=Simplify) |
| CareSource | 2026 Summer Internship - Data Science | Remote | 10/18/2025 | [APPLY](https://caresource.wd1.myworkdayjobs.com/en-US/caresource/job/Remote/XMLNAME-2026-Summer-Internship---Data-Science_R10679?utm_source=Simplify&ref=Simplify) |
| Token Metrics | Crypto Data Scientist / Machine Learning - LLM Engineer Intern | Remote | 10/18/2025 | [APPLY](https://jobs.lever.co/tokenmetrics/62b16e29-602d-4f52-ba4b-89c02b6dee41?utm_source=Simplify&ref=Simplify) |
| Token Metrics | Crypto Quantitative Analyst Intern | Remote | 10/18/2025 | [APPLY](https://jobs.lever.co/tokenmetrics/8b78659b-0454-4954-9e21-c42c4d5c34fe?utm_source=Simplify&ref=Simplify) |
| Zipcar | Software Engineer Co-Op- Billing | Boston | 10/17/2025 | [APPLY](https://www.zipcar.com) |
| Toyota Research Institute | Human Aware Interaction and Learning – Research Intern | Cambridge, MA | 10/17/2025 | [APPLY](https://jobs.lever.co/tri/b012c063-b8a8-454b-8026-6a8cf8a4e5fc/apply?utm_source=Simplify&ref=Simplify) |
| Zipcar | Software Engineer Co-Op-Billing | Boston, MA | 10/17/2025 | [APPLY](https://avisbudget.wd1.myworkdayjobs.com/Zipcar_Careers/job/35-Thomson-Pl-Boston-02210/Software-Engineer-Co-Op--Billing_R0181488?utm_source=Simplify&ref=Simplify) |
| PTC | Software Engineering Intern | Boston, MA | 10/16/2025 | [APPLY](https://www.ptc.com) |
| PTC | Software Development Intern | Boston, MA | 10/16/2025 | [APPLY](https://www.ptc.com) |
| PTC | Software Engineering Intern | Boston, MA | 10/16/2025 | [APPLY](https://www.ptc.com) |
| Zipcar | Software Engineer Co-Op- B2B | Boston | 10/16/2025 | [APPLY](https://www.zipcar.com) |
| Zus Health | Data Platform Software Engineering Co-op | 4 locations Boston | 10/16/2025 | [APPLY](https://jobs.lever.co/zushealth/54557977-eaa9-4ae9-aadd-9a1ac9551575?utm_source=github-vansh-ouckah) |
| PTC | Software Development Intern | Boston, MA | 10/16/2025 | [APPLY](https://ptc.wd1.myworkdayjobs.com/ptc/job/Boston-MA-USA/Software-Development-Intern_JR110934?utm_source=github-vansh-ouckah) |
| Leidos | Software Engineer Intern | Remote | 10/16/2025 | [APPLY](https://leidos.wd5.myworkdayjobs.com/external/job/6314-RemoteTeleworker-US/Software-Engineer-Intern_R-00168796?utm_source=github-vansh-ouckah) |
| GE Vernova | GE Vernova Sustainability AI Solutions Intern - Summer 2026 | Cambridge, MA | 10/16/2025 | [APPLY](https://gevernova.wd5.myworkdayjobs.com/only_confidential_executive_recruiting/job/Cambridge/GE-Vernova-Sustainability-AI-Solutions-Intern---Summer-2026_R5020619-1?utm_source=Simplify&ref=Simplify) |
| Airspace Intelligence | Software Engineer Co-Op – Defense | Boston, MA | 10/16/2025 | [APPLY](https://jobs.ashbyhq.com/airspace-intelligence.com/c2ef5338-def2-4370-8ab0-0775466d8bf8?utm_source=Simplify&ref=Simplify) |
| Formlabs | Hardware Test Engineering Intern (Winter/Spring 2026) | Somerville, MA | 10/16/2025 | [APPLY](https://careers.formlabs.com/job/7271951/apply/?gh_jid=7271951) |
| Formlabs | Program Management - Global Sourcing Intern (Winter/Spring 2026) | Boston, MA | 10/16/2025 | [APPLY](https://careers.formlabs.com/job/7190788/apply/?gh_jid=7190788) |
| Formlabs | Global Operations Sourcing Intern (Winter/Spring 2026) | Boston, MA | 10/16/2025 | [APPLY](https://careers.formlabs.com/job/7190913/apply/?gh_jid=7190913) |
| Air Space Intelligence | Software Engineer Co-Op Defense | Boston, US | 10/15/2025 | [APPLY](https://www.airspace-intelligence.com/) |
| Fidelity Investments | Co-op - Software Engineer | Boston, MA | 10/15/2025 | [APPLY](https://fidelity.com/) |
| Zus Health | Data Platform Software Engineering Co-op | Boston, MA | 10/15/2025 | [APPLY](https://zushealth.com) |
| Zus Health | Fullstack Software Engineering Co-op | Boston, MA | 10/15/2025 | [APPLY](https://zushealth.com) |
| Lazard | Quantitative Researcher Intern | Boston | 10/15/2025 | [APPLY](https://lazard-careers.tal.net/vx/mobile-0/appcentre-ext/brand-4/candidate/so/pm/1/pl/2/opp/3876-2026-Summer-Internship-Quantitative-Researcher/en-GB?utm_source=github-vansh-ouckah) |
| ConnectPrep | Data Analyst Intern | Boston, MA | 10/15/2025 | [APPLY](https://apply.workable.com/connectprep/j/390EB8941D/apply?utm_source=github-vansh-ouckah) |
| Lazard | 2026 Summer Internship - Quantitative Researcher | Boston, MA | 10/15/2025 | [APPLY](https://lazard-careers.tal.net/vx/mobile-0/appcentre-ext/brand-4/candidate/so/pm/1/pl/2/opp/3876-2026-Summer-Internship-Quantitative-Researcher/en-GB?utm_source=Simplify&ref=Simplify) |
| Bose | Embedded Firmware Intern | Framingham, MA | 10/15/2025 | [APPLY](https://boseallaboutme.wd503.myworkdayjobs.com/Bose_Careers/job/US-MA---Framingham/Embedded-Firmware-intern_R28337?utm_source=Simplify&ref=Simplify) |
| Formlabs | Hardware R&D Engineering Intern (Winter/Spring 2026) | Somerville, MA | 10/15/2025 | [APPLY](https://careers.formlabs.com/job/7233962/apply/?gh_jid=7233962) |
| CarGurus | Data Platform Engineer II | Boston, Massachusetts | 10/15/2025 | [APPLY](https://careers.cargurus.com/us/en/job/7264613?gh_jid=7264613) |
| PTC | Software Engineering Intern | Boston, MA | 10/14/2025 | [APPLY](https://www.ptc.com) |
| Highmark Health | Data Science Research Intern - Data Science | Massachusetts | 10/14/2025 | [APPLY](https://highmarkhealth.wd1.myworkdayjobs.com/highmark/job/PA-Working-at-Home---Pennsylvania/Summer-2026-Data-Science-Research-Graduate-Intern_J270569?utm_source=Simplify&ref=Simplify) |
| LabCorp | Intern – Real-World Data Analytics | Remote in USA | 10/14/2025 | [APPLY](https://labcorp.wd1.myworkdayjobs.com/external/job/Remote_United-States/Intern---Real-World-Data-Analytics_2533322?utm_source=Simplify&ref=Simplify) |
| RTX | Software Engineer Intern - Multiple Teams | Marlborough, MA | 10/14/2025 | [APPLY](https://globalhr.wd5.myworkdayjobs.com/rec_rtx_ext_gateway/job/MA801-Marlborough-MA-1001-Boston-Post-Road-Building-2-Marlborough-MA-01752-USA/XMLNAME-2026-Intern---Software-Engineer-Intern---Onsite--MA-_01799047?utm_source=Simplify&ref=Simplify) |
| Warner Bros. | WB Games Software Engineering Intern Co-op - Multiple Teams | Needham, MA | 10/14/2025 | [APPLY](https://warnerbros.wd5.myworkdayjobs.com/global/job/MA-Needham-117-Kendrick-St/WB-Games-Software-Engineering-Intern-Co-op--Needham--MA---January-May-2026_R000098574?utm_source=Simplify&ref=Simplify) |
| Warner Bros. | WB Games Software Engineering Intern Co-op - Multiple Teams | Needham, MA | 10/14/2025 | [APPLY](https://warnerbros.wd5.myworkdayjobs.com/global/job/MA-Needham-117-Kendrick-St/WB-Games-Software-Engineering-Intern-Co-op--Needham--MA---June-December-2026_R000098591?utm_source=Simplify&ref=Simplify) |
| PTC | Software Engineer Intern | Boston, MA | 10/14/2025 | [APPLY](https://ptc.wd1.myworkdayjobs.com/ptc/job/Boston-MA-USA/Software-Engineer-Intern_JR110885?utm_source=Simplify&ref=Simplify) |
| Formlabs | Manufacturing Engineering Intern (Spring/Summer 2026) | Somerville, MA | 10/14/2025 | [APPLY](https://careers.formlabs.com/job/7083351/apply/?gh_jid=7083351) |
| Formlabs | Manufacturing Test Software Intern (Winter/Spring 2026) | Somerville, MA | 10/14/2025 | [APPLY](https://careers.formlabs.com/job/7284267/apply/?gh_jid=7284267) |
| Formlabs | Industrial Design Intern (Winter/Spring 2026) | Somerville, MA | 10/14/2025 | [APPLY](https://careers.formlabs.com/job/7269786/apply/?gh_jid=7269786) |
| Wealth.com | Software Engineer Intern | Remote | 10/13/2025 | [APPLY](https://jobs.lever.co/WealthFinancialTechnologies/a4fe7c66-0e2a-4e06-a029-2f70c30a8e0a?utm_source=github-vansh-ouckah) |
| Hone Health | Data Science Intern | Remote in USA | 10/13/2025 | [APPLY](https://job-boards.greenhouse.io/honehealth/jobs/4945568008?utm_source=Simplify&ref=Simplify) |
| Sephora | IT Warehouse & Distribution Automation Intern | Remote | 10/11/2025 | [APPLY](https://join.sephora.com/careers/job/790312348148?utm_source=github-vansh-ouckah) |
| Eversource Energy | Software Engineering Intern - Software Engineering | Norwood, MA | 10/11/2025 | [APPLY](https://eversource.wd1.myworkdayjobs.com/ExternalSite/job/Windsor-CT/Summer-2026-Software-Engineering-Intern_R-028852?utm_source=github-vansh-ouckah) |
| CenturyLink | Intern - Software Developer | Remote in USA | 10/11/2025 | [APPLY](https://internaljobs.centurylink.com/job/Remote-Intern-Software-Developer-Summer-2026/1333501200/?ats=successfactors&utm_source=github-vansh-ouckah) |
| Biogen | Machine Learning Co-op | Cambridge, MA | 10/11/2025 | [APPLY](https://biibhr.wd3.myworkdayjobs.com/en-US/external/job/Cambridge-MA/Co-op--Machine-Learning_REQ21752?utm_source=github-vansh-ouckah) |
| Altice USA | Intern – Customer Care | Wakefield, MA | 10/11/2025 | [APPLY](https://www.alticeusacareers.com/job/Bethpage-Intern-Customer-Care-NY-11714/1333655100/?ats=successfactors&utm_source=Simplify&ref=Simplify) |
| Highmark Health | Data Science Intern - Multiple Teams | Massachusetts | 10/11/2025 | [APPLY](https://highmarkhealth.wd1.myworkdayjobs.com/highmark/job/PA-Working-at-Home---Pennsylvania/Summer-2026-Data-Science-Graduate-Intern_J270573?utm_source=Simplify&ref=Simplify) |
| Lumen Technologies | Intern – Product Marketing - Summer 2026 | Remote in USA | 10/11/2025 | [APPLY](https://jobs.lumen.com/global/en/job/340176?utm_source=Simplify&ref=Simplify) |
| Leidos | Cyber AI/ML Intern - Cyber AI - Multiple Teams | Remote in USA | 10/11/2025 | [APPLY](https://leidos.wd5.myworkdayjobs.com/External/job/6314-RemoteTeleworker-US/XMLNAME---Cyber-AI-ML-Intern-_R-00168344?utm_source=Simplify&ref=Simplify) |
| CenturyLink | Intern – AI Enablement and Technology Transformation - Summer 2026 | Remote in USA | 10/11/2025 | [APPLY](https://internaljobs.centurylink.com/job/Remote-Intern-AI-Enablement-and-Technology-Transformation-Summer-2026/1333819500/?ats=successfactors&utm_source=Simplify&ref=Simplify) |
| Lumen Technologies | Intern – AI Enablement and Technology Transformation - Summer 2026 | Remote in USA | 10/11/2025 | [APPLY](https://jobs.lumen.com/global/en/job/340242?utm_source=Simplify&ref=Simplify) |
| Athena Health | Software Engineering Intern - Multiple Teams | Boston, MA | 10/11/2025 | [APPLY](https://athenahealth.wd1.myworkdayjobs.com/en-US/External/job/Boston-MA/XMLNAME-2026-Summer-Software-Engineering-Intern_R13615?utm_source=Simplify&ref=Simplify) |
| Research Innovations | Software Development Engineering in Test Internship Summer 2026 - EC2118 | Remote | 10/10/2025 | [APPLY](https://www.researchinnovations.com/) |
| State Street | Product Intern - Product Team | Quincy, MA | 10/10/2025 | [APPLY](https://statestreet.wd1.myworkdayjobs.com/en-US/Global/job/Quincy-Massachusetts/State-Street-Product-Office---Summer-Internship-2026_R-778817?utm_source=Simplify&ref=Simplify) |
| Eversource Energy | Software Engineering Intern | Westwood, MA | 10/10/2025 | [APPLY](https://eversource.wd1.myworkdayjobs.com/ExternalSite/job/Windsor-CT/Summer-2026-Software-Engineering-Intern_R-028852?utm_source=Simplify&ref=Simplify) |
| NVIDIA | PhD Research Intern - Security and Privacy | Westford, MA | 10/10/2025 | [APPLY](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/PhD-Research-Intern--Security-and-Privacy---2026_JR2004956?utm_source=Simplify&ref=Simplify) |
| Altice USA | Intern - Network Planning & Engineering - Network Planning - Engineering | Wakefield, MA | 10/10/2025 | [APPLY](https://www.alticeusacareers.com/job/Bethpage-Intern-Network-Planning-&-Engineering-NY-11714/1332899600/?ats=successfactors&utm_source=Simplify&ref=Simplify) |
| CenturyLink | Intern - Product Marketing - Product Marketing | Remote in USA | 10/10/2025 | [APPLY](https://internaljobs.centurylink.com/job/Remote-Intern-Product-Marketing-Summer-2026/1333709700/?ats=successfactors&utm_source=Simplify&ref=Simplify) |
| CenturyLink | Intern - Data Enablement: System Architecture - Multiple Teams | Remote in USA | 10/10/2025 | [APPLY](https://internaljobs.centurylink.com/job/Remote-Intern-Data-Enablement-System-Architecture-Summer-2026/1333645300/?ats=successfactors&utm_source=Simplify&ref=Simplify) |
| Lumen Technologies | Intern – Data Enablement: System Architecture - Summer 2026 | Remote in USA | 10/10/2025 | [APPLY](https://jobs.lumen.com/global/en/job/340244?utm_source=Simplify&ref=Simplify) |
| Fresenius Medical Care | Machine Learning Analytics Intern/Co-op - Home Therapy Product Management | Andover, MA | 10/10/2025 | [APPLY](https://freseniusmedicalcare.wd3.myworkdayjobs.com/fme/job/Lawrence-MA-USA/Machine-Learning-Analytics-Co-op--DSS_R0222634?utm_source=Simplify&ref=Simplify) |
| Crowdstrike | Sales Excellence Data Analytics Intern - Multiple Teams | Remote in USA | 10/10/2025 | [APPLY](https://crowdstrike.wd5.myworkdayjobs.com/crowdstrikecareers/job/USA---Remote/Sales-Excellence-Data-Analytics-Intern---Summer-2026--Remote-_R25067-1?utm_source=Simplify&ref=Simplify) |
| Fresenius Medical Care | Data Analytics Engineering Intern/Co-op - Home Therapy Analytics - Product Management | Andover, MA | 10/10/2025 | [APPLY](https://freseniusmedicalcare.wd3.myworkdayjobs.com/fme/job/Lawrence-MA-USA/Data-Anayltics-Engineering-Co-op_R0222631?utm_source=Simplify&ref=Simplify) |
| CenturyLink | Intern - Software Developer - Multiple Teams | Remote in USA | 10/10/2025 | [APPLY](https://internaljobs.centurylink.com/job/Remote-Intern-Software-Developer-Summer-2026/1333501200/?ats=successfactors&utm_source=Simplify&ref=Simplify) |
| Lumen Technologies | Intern – Software Developer - Summer 2026 | Remote in USA | 10/10/2025 | [APPLY](https://jobs.lumen.com/global/en/job/340209?utm_source=Simplify&ref=Simplify) |
| Chess | Engineering Internship, Backend | Remote in USA | 10/10/2025 | [APPLY](https://ats.rippling.com/chess/jobs/f199901c-ee5f-4846-97ed-b2252be44a30?utm_source=Simplify&ref=Simplify) |
| Businessolver | Software Engineer Intern - Java - SQL | Remote in USA | 10/10/2025 | [APPLY](https://job-boards.greenhouse.io/businessolverinvitationonly/jobs/6176718?utm_source=Simplify&ref=Simplify) |
| Formlabs | Electrical Engineering Intern (Winter/Spring 2026) | Somerville, MA | 10/10/2025 | [APPLY](https://careers.formlabs.com/job/7286400/apply/?gh_jid=7286400) |
| Lumen Technologies | Strategic Fiber Planning Intern | Remote in USA | 10/09/2025 | [APPLY](https://jobs.lumen.com/global/en/job/340218?utm_source=github-vansh-ouckah) |
| Fresenius Medical Care | Reciprocity Embedded Software Engineer Co-op | Lawrence, MA | 10/09/2025 | [APPLY](https://freseniusmedicalcare.wd3.myworkdayjobs.com/en-US/fme/job/Lawrence-MA-USA/Reciprocity-Embedded-Software-Engineer-Co-op--DSS_R0222635?utm_source=github-vansh-ouckah) |
| Chess.com | Engineering Intern, Backend | Remote | 10/09/2025 | [APPLY](https://ats.rippling.com/en-GB/chess/jobs/f199901c-ee5f-4846-97ed-b2252be44a30?utm_source=github-vansh-ouckah) |
| Altice USA | Intern – Junior Systems Analyst | Wakefield, MA | 10/09/2025 | [APPLY](https://www.alticeusacareers.com/job/Golden-Intern-Jr-Systems-Analyst-CO-80401/1332889100/?ats=successfactors&utm_source=Simplify&ref=Simplify) |
| Versapay | Product Management Intern - Product Management | Remote in USA | 10/09/2025 | [APPLY](https://jobs.lever.co/versapay/5e152057-a83d-49f7-95d2-5406d58823d0/apply?utm_source=Simplify&ref=Simplify) |
| Klaviyo | Product Marketing Intern/Co-op - Multiple Teams | Boston, MA | 10/09/2025 | [APPLY](https://job-boards.greenhouse.io/klaviyocampus/jobs/7483172003?utm_source=Simplify&ref=Simplify) |
| CenturyLink | Intern - Data Analyst - Multiple Teams | Remote in USA | 10/09/2025 | [APPLY](https://internaljobs.centurylink.com/job/Remote-Intern-Data-Analyst-Summer-2026/1333099400/?ats=successfactors&utm_source=Simplify&ref=Simplify) |
| Lumen Technologies | Intern – Planning Engineer - Summer 2026 | Remote in USA | 10/09/2025 | [APPLY](https://jobs.lumen.com/global/en/job/340262?utm_source=Simplify&ref=Simplify) |
| Highmark Health | Management (AI Products) Graduate Intern | Remote in USA | 10/09/2025 | [APPLY](https://highmarkhealth.wd1.myworkdayjobs.com/en-US/highmark/job/PA-Working-at-Home---Pennsylvania/Summer-2026-Management--AI-Products--Graduate-Intern_J269793?utm_source=Simplify&ref=Simplify) |
| Lumen Technologies | Intern – Senior Planning Engineer - Summer 2026 | Remote in USA | 10/09/2025 | [APPLY](https://jobs.lumen.com/global/en/job/340234?utm_source=Simplify&ref=Simplify) |
| Fresenius Medical Care | Reciprocity Embedded Software Engineer Co-op- DSS | Lawrence, MA | 10/09/2025 | [APPLY](https://freseniusmedicalcare.wd3.myworkdayjobs.com/en-US/fme/job/Lawrence-MA-USA/Reciprocity-Embedded-Software-Engineer-Co-op--DSS_R0222635?utm_source=Simplify&ref=Simplify) |
| Lumen Technologies | Intern - Network Transformation - DevOps Engineering | Remote in USA | 10/09/2025 | [APPLY](https://jobs.lumen.com/global/en/job/340211?utm_source=Simplify&ref=Simplify) |
| Fresenius Medical Care North America | Reciprocity Embedded Software Engineer Co-op- DSS | Lawrence, MA | 10/08/2025 | [APPLY](https://fmcna.com) |
| Highmark Health | Evaluation Analytics Graduate Intern - Analytics | Massachusetts | 10/08/2025 | [APPLY](https://highmarkhealth.wd1.myworkdayjobs.com/highmark/job/PA-Working-at-Home---Pennsylvania/Summer-2026-Evaluation-Analytics-Graduate-Intern_J270014-1?utm_source=Simplify&ref=Simplify) |
| PathAI | Machine Learning Intern/Co-op - Multiple Teams | Boston, MA, Remote in US | 10/08/2025 | [APPLY](https://www.pathai.com/careers/8202342002?gh_jid=8202342002&utm_source=Simplify&ref=Simplify) |
| Boston Consulting Group | AI Engineer – Internship - BCG X | Boston, MA | 10/08/2025 | [APPLY](https://careers.bcg.com/global/en/job/55514?utm_source=Simplify&ref=Simplify) |
| Meta | Research Scientist Intern - AI Alignment | Boston, MA | 10/08/2025 | [APPLY](https://www.metacareers.com/jobs/1782902493113620?utm_source=Simplify&ref=Simplify) |
| CenturyLink | Intern – Big Data Developer - Summer 2026 | Remote in USA | 10/08/2025 | [APPLY](https://internaljobs.centurylink.com/job/Remote-Intern-Big-Data-Developer-Summer-2026/1332626500/?ats=successfactors&utm_source=Simplify&ref=Simplify) |
| Lumen Technologies | Intern – Big Data Developer - Summer 2026 | Remote in USA | 10/08/2025 | [APPLY](https://jobs.lumen.com/global/en/job/340255?utm_source=Simplify&ref=Simplify) |
| Rockwell Automation | Co-op – Firmware Engineering - Multiple Teams | Lowell, MA | 10/08/2025 | [APPLY](https://rockwellautomation.wd1.myworkdayjobs.com/en-US/External_Rockwell_Automation/job/Chelmsford-Massachusetts-United-States/Co-op--Firmware-Engineering---Chelmsford--January-2026-to-August-2026-_R25-7012-1?utm_source=Simplify&ref=Simplify) |
| ZOLL Medical Corporation | Software Intern | Lowell, MA | 10/08/2025 | [APPLY](https://zoll.wd5.myworkdayjobs.com/en-US/ZOLLMedicalCorp/job/Chelmsford-MA/Software-Intern_R16943?utm_source=Simplify&ref=Simplify) |
| Formlabs | Build Team Intern (Winter/Spring 2026) | Somerville, MA | 10/08/2025 | [APPLY](https://careers.formlabs.com/job/7215024/apply/?gh_jid=7215024) |
| Formlabs | Mechanical Engineering Intern (Winter/Spring 2026) | Somerville, MA | 10/08/2025 | [APPLY](https://careers.formlabs.com/job/7095197/apply/?gh_jid=7095197) |
| Formlabs | People Analytics MBA Intern (Fall 2025 Part-Time) | Somerville, MA | 10/08/2025 | [APPLY](https://careers.formlabs.com/job/7263134/apply/?gh_jid=7263134) |
| Formlabs | Print Production Intern (Winter/Spring 2026) | Somerville, MA | 10/08/2025 | [APPLY](https://careers.formlabs.com/job/7217328/apply/?gh_jid=7217328) |
| Formlabs | Video Content Creator Intern (Winter/Spring 2026) | Somerville, MA | 10/08/2025 | [APPLY](https://careers.formlabs.com/job/7134956/apply/?gh_jid=7134956) |
| Wealth | Software Engineer Internship | Remote | 10/07/2025 | [APPLY](https://wealth.com) |
| CenturyLink | Intern – Product Management - Multiple Teams | Remote in USA | 10/07/2025 | [APPLY](https://internaljobs.centurylink.com/job/Remote-Intern-Product-Management-Summer-2026/1332255900/?ats=successfactors&utm_source=Simplify&ref=Simplify) |
| CenturyLink | Intern – Markops Reporting Analyst - Summer 2026 | Remote in USA | 10/07/2025 | [APPLY](https://internaljobs.centurylink.com/job/Remote-Intern-MarkOps-Reporting-Analyst-Summer-2026/1332335800/?ats=successfactors&utm_source=Simplify&ref=Simplify) |
| Lumen Technologies | Intern – Data Analyst - Summer 2026 | Remote in USA | 10/07/2025 | [APPLY](https://jobs.lumen.com/global/en/job/340240?utm_source=Simplify&ref=Simplify) |
| Lumen Technologies | Intern – Data Governance - Summer 2026 | Remote in USA | 10/07/2025 | [APPLY](https://jobs.lumen.com/global/en/job/340246?utm_source=Simplify&ref=Simplify) |
| Lumen Technologies | Intern – Markops Reporting Analyst - Summer 2026 | Remote in USA | 10/07/2025 | [APPLY](https://jobs.lumen.com/global/en/job/340216?utm_source=Simplify&ref=Simplify) |
| CenturyLink | Intern - Data Governance - Multiple Teams | Remote in USA | 10/07/2025 | [APPLY](https://internaljobs.centurylink.com/job/Remote-Intern-Data-Governanace-Summer-2026/1332307400/?ats=successfactors&utm_source=Simplify&ref=Simplify) |
| CenturyLink | Intern – Software Development Engineer - Digital Platform and Architecture | Remote in USA | 10/07/2025 | [APPLY](https://internaljobs.centurylink.com/job/Remote-Intern-Software-Development-Engineer-Summer-2026/1332369700/?ats=successfactors&utm_source=Simplify&ref=Simplify) |
| Lumen Technologies | Intern – Software Development Engineer - Summer 2026 | Remote in USA | 10/07/2025 | [APPLY](https://jobs.lumen.com/global/en/job/340233?utm_source=Simplify&ref=Simplify) |
| Lumen Technologies | Intern – Back-End Developer - Summer 2026 | Remote in USA | 10/07/2025 | [APPLY](https://jobs.lumen.com/global/en/job/340264?utm_source=Simplify&ref=Simplify) |
| Lumen Technologies | Intern – Software Developer - Summer 2026 | Remote in USA | 10/07/2025 | [APPLY](https://jobs.lumen.com/global/en/job/340179?utm_source=Simplify&ref=Simplify) |
| CenturyLink | Intern – Software Developer - Summer 2026 | Remote in USA | 10/07/2025 | [APPLY](https://internaljobs.centurylink.com/job/Remote-Intern-Software-Developer-Summer-2026/1332268100/?ats=successfactors&utm_source=Simplify&ref=Simplify) |
| Khan Academy | Software Engineer Intern - Multiple Teams | Remote in USA | 10/07/2025 | [APPLY](https://job-boards.greenhouse.io/khanacademy/jobs/7258549?utm_source=Simplify&ref=Simplify) |
| State Street | Desktop Engineering Associate, Co-Op | Quincy, MA | 10/06/2025 | [APPLY](https://statestreet.wd1.myworkdayjobs.com/en-US/Global/job/Quincy-Massachusetts/Desktop-Engineering-Associate--Co-Op_R-778571?utm_source=github-vansh-ouckah) |
| Sephora | Machine Learning Engineer Intern, Technology | Remote | 10/06/2025 | [APPLY](https://join.sephora.com/careers/job/790312030968?utm_source=github-vansh-ouckah) |
| Datadog | Sales Development Representative - Summer 2026 Graduates (Spanish Speaking) | Boston, Massachusetts, USA | 10/06/2025 | [APPLY](https://careers.datadoghq.com/detail/7251992/?gh_jid=7251992) |
| Datadog | Sales Development Representative - Summer 2026 Graduates (Portuguese Speaking) | Boston, Massachusetts, USA | 10/06/2025 | [APPLY](https://careers.datadoghq.com/detail/7252012/?gh_jid=7252012) |
| Datadog | Sales Development Representative - Summer 2026 Graduates (Boston) | Boston, Massachusetts, USA | 10/06/2025 | [APPLY](https://careers.datadoghq.com/detail/7248738/?gh_jid=7248738) |
| State Street | Software Engineer Intern/Co-op - Charles River Development | Burlington, MA | 10/05/2025 | [APPLY](https://statestreet.wd1.myworkdayjobs.com/en-US/Global/job/Burlington-Massachusetts/Software-Engineer-CO-OP--CRD--Jan-Jun_R-778704?utm_source=Simplify&ref=Simplify) |
| Philips | Co-op – Healthcare Data Scientist - Healthcare Data Science | Cambridge, MA | 10/05/2025 | [APPLY](https://philips.wd3.myworkdayjobs.com/jobs-and-careers/job/Cambridge-US/XMLNAME--Co-op---Healthcare-Data-Scientist---Cambridge--MA_563021?utm_source=Simplify&ref=Simplify) |
| Philips | Co-op – Software Development Engineer - Automation | Cambridge, MA | 10/05/2025 | [APPLY](https://philips.wd3.myworkdayjobs.com/jobs-and-careers/job/Cambridge-US/Co-op---Software-Development-Engineer--Automation----Cambridge--MA---January-August-2026_564729?utm_source=Simplify&ref=Simplify) |
| Tamr | Front End Software Engineering - React.js Co-op - 2026 | Cambridge, MA | 10/04/2025 | [APPLY](https://www.tamr.com) |
| Vertex Pharmaceuticals | Intern 2026 - Data Technology - Engineering | Boston, MA | 10/04/2025 | [APPLY](https://vrtx.wd501.myworkdayjobs.com/vertex_careers/job/Boston-MA/Vertex-Summer-Intern-2026--DTE--Data--Technology--and-Engineering-_REQ-26580?utm_source=Simplify&ref=Simplify) |
| Philips | Co-op – Software System Integration - Multiple Teams | Cambridge, MA | 10/04/2025 | [APPLY](https://philips.wd3.myworkdayjobs.com/jobs-and-careers/job/Cambridge-US/Co-op---Software-System-Integration---Cambridge--MA---January-August-2026_564725?utm_source=Simplify&ref=Simplify) |
| Tamr | Front End Software Engineer Intern/Co-op - React | Cambridge, MA | 10/04/2025 | [APPLY](https://jobs.lever.co/tamr/b12f76cf-e55b-4650-bb4e-349e0aa97949/apply?utm_source=Simplify&ref=Simplify) |
| Philips | Co-op – Software Engineering - Multiple Teams | Cambridge, MA | 10/04/2025 | [APPLY](https://philips.wd3.myworkdayjobs.com/jobs-and-careers/job/Cambridge-US/Co-op---Software-Engineering---Cambridge--MA---June---December-2025_562524?utm_source=Simplify&ref=Simplify) |
| Highmark Health | Data Test Engineering Intern - Multiple Teams | Massachusetts | 10/03/2025 | [APPLY](https://highmarkhealth.wd1.myworkdayjobs.com/highmark/job/PA-Working-at-Home---Pennsylvania/Summer-2026-Non-Functional-Data-Test-Engineering-Undergraduate-Intern_J270317?utm_source=Simplify&ref=Simplify) |
| Iron Mountain | Finance & Analytics Intern - Multiple Teams | Boston, MA | 10/03/2025 | [APPLY](https://ironmountain.wd5.myworkdayjobs.com/iron-mountain-jobs/job/US--MA--Remote/Finance---Analytics-Intern--Summer-2026-_J0093381?utm_source=Simplify&ref=Simplify) |
| Bristol Myers Squibb | Graduate Data Science Intern - Pharmacometrics Programming | Cambridge, MA | 10/03/2025 | [APPLY](https://bristolmyerssquibb.wd5.myworkdayjobs.com/bms/job/Cambridge-Crossing---MA---US/Summer-2026---Graduate-Data-Science---Pharmacometrics-Programming-Internship_R1595674?utm_source=Simplify&ref=Simplify) |
| Vertex Pharmaceuticals | Intern - Clinical Data Management | Boston, MA | 10/03/2025 | [APPLY](https://vrtx.wd501.myworkdayjobs.com/vertex_careers/job/Boston-MA/Vertex-Summer-Intern-2026--Clinical-Data-Management---Metrics_REQ-26586?utm_source=Simplify&ref=Simplify) |
| Fidelity | Quantitative Development & Data Science Internship | Boston, MA | 10/03/2025 | [APPLY](https://fmr.wd1.myworkdayjobs.com/en-US/targeted/job/Boston-MA/Quantitative-Development---Data-Science-Internship_2115892?utm_source=Simplify&ref=Simplify) |
| RTX | Intern - Full Stack Developer | Cambridge, MA | 10/03/2025 | [APPLY](https://globalhr.wd5.myworkdayjobs.com/rec_rtx_ext_gateway/job/MA105-BBN-Headquarters-10-Moulton-Street---Cambridge-MA-02138-USA/Summer-2026-Intern---Full-Stack-Developer--Onsite-_01795503?utm_source=Simplify&ref=Simplify) |
| Datadog | Software Engineering Intern (Summer) | Boston, Massachusetts | 10/03/2025 | [APPLY](https://careers.datadoghq.com/detail/7158137/?gh_jid=7158137) |
| State Street | Software Engineer - Co-Op | Quincy, Massachusetts | 10/02/2025 | [APPLY](https://www.statestreet.com) |
| RTX | Software Engineer Intern - Multiple Teams | Marlborough, MA | 10/02/2025 | [APPLY](https://globalhr.wd5.myworkdayjobs.com/rec_rtx_ext_gateway/job/MA801-Marlborough-MA-1001-Boston-Post-Road-Building-2-Marlborough-MA-01752-USA/XMLNAME-2026-Intern---Software-Engineer-Intern---Onsite--MA-_01797376?utm_source=Simplify&ref=Simplify) |
| Formlabs | Manufacturing Test Software Intern - Winter/Spring 2026 | Somerville, MA | 10/01/2025 | [APPLY](https://formlabs.com) |
| State Street | Software Engineer - Co-Op | Quincy, Massachusetts | 10/01/2025 | [APPLY](https://www.statestreet.com) |
| State Street | Software Engineer - Co-Op | Quincy, Massachusetts | 10/01/2025 | [APPLY](https://www.statestreet.com) |
| Datacor | Internship Program | Remote | 10/01/2025 | [APPLY](https://job-boards.greenhouse.io/datacor/jobs/4918298007?utm_source=github-vansh-ouckah) |
| Rockwell Automation | Intern - Product Management | Lowell, MA | 10/01/2025 | [APPLY](https://rockwellautomation.wd1.myworkdayjobs.com/en-US/External_Rockwell_Automation/job/Chelmsford-Massachusetts-United-States/Intern--Product-Management_R25-7776-1?utm_source=Simplify&ref=Simplify) |
| Datacor | Internship Program - Multiple Teams | Remote in USA | 10/01/2025 | [APPLY](https://job-boards.greenhouse.io/datacor/jobs/4918298007?utm_source=Simplify&ref=Simplify) |
| State Street | AI Enablement Engineer – Co-Op | Quincy, MA | 10/01/2025 | [APPLY](https://statestreet.wd1.myworkdayjobs.com/en-US/Global/job/Quincy-Massachusetts/AI-Enablement-Engineer--Co-Op_R-778365?utm_source=Simplify&ref=Simplify) |
| Autodesk | Intern - AI Agent and Knowledge Graphs - Research - AI Technologies | Boston, MA | 10/01/2025 | [APPLY](https://autodesk.wd1.myworkdayjobs.com/en-US/uni/job/Boston-MA-USA/Intern--AI-Agent-and-Knowledge-Graphs_25WD91982?utm_source=Simplify&ref=Simplify) |
| Rockwell Automation | Intern - Test Engineering - Multiple Teams | Lowell, MA | 10/01/2025 | [APPLY](https://rockwellautomation.wd1.myworkdayjobs.com/en-US/External_Rockwell_Automation/job/United-States-of-America-Chelmsford/Intern--Test-Engineering---Chelmsford_R25-8009-1?utm_source=Simplify&ref=Simplify) |
| State Street | Efx Developer – Co-Op | Quincy, MA | 10/01/2025 | [APPLY](https://statestreet.wd1.myworkdayjobs.com/en-US/Global/job/Quincy-Massachusetts/eFX-Developer--Co-Op_R-778439?utm_source=Simplify&ref=Simplify) |
| Datadog | Enterprise Security Sales Specialist | Boston, Massachusetts, USA<br>+1 more | 10/01/2025 | [APPLY](https://careers.datadoghq.com/detail/7129425/?gh_jid=7129425) |
| Datadog | Product Solutions Architect 3 - APM | Boston, Massachusetts, USA<br>+1 more | 10/01/2025 | [APPLY](https://careers.datadoghq.com/detail/6825839/?gh_jid=6825839) |
| Datadog | Product Solutions Architect (Serverless) | Boston, Massachusetts, USA<br>+1 more | 10/01/2025 | [APPLY](https://careers.datadoghq.com/detail/7191402/?gh_jid=7191402) |
| Datadog | Security Engineer II - Cloud Security | Boston, Massachusetts, USA<br>+3 more | 10/01/2025 | [APPLY](https://careers.datadoghq.com/detail/7205511/?gh_jid=7205511) |
| Lean TECHniques | Software Intern - Summer 2026 | Remote | 09/30/2025 | [APPLY](https://leantechniques.com/) |
| State Street | Software Engineer - Co-Op | Quincy, Massachusetts | 09/30/2025 | [APPLY](https://www.statestreet.com) |
| Zurich Insurance | Precision Agriculture Internship - Summer 2026 | Andover, MN | 09/30/2025 | [APPLY](https://www.careers.zurich.com/job/Virtual-Precision-Agriculture-Internship-(Summer-2026)-IA/1328202457/?ats=successfactors&utm_source=Simplify&ref=Simplify) |
| Cotiviti | Intern – Agentic AI Research | Remote in USA | 09/30/2025 | [APPLY](https://careers-cotiviti.icims.com/jobs/16718/job?mobile=true&needsRedirect=false&utm_source=Simplify&ref=Simplify) |
| Audax Group | AI Engineer Intern - Multiple Teams | Boston, MA | 09/30/2025 | [APPLY](https://job-boards.greenhouse.io/audaxgroup/jobs/4613476005?utm_source=Simplify&ref=Simplify) |
| Comcast | Machine Learning Research Intern - Multiple Teams | Remote in USA | 09/30/2025 | [APPLY](https://comcast.wd5.myworkdayjobs.com/Comcast_Careers/job/Virtual/Comcast-Machine-Learning-Research---Engineering-Intern_R420084?utm_source=Simplify&ref=Simplify) |
| State Street | Emerging Technology Governance, Co-Op | Boston, MA, Quincy | 09/30/2025 | [APPLY](https://statestreet.wd1.myworkdayjobs.com/en-US/Global/job/BOSTON/Emerging-Technology-Governance--Co-Op_R-778255?utm_source=Simplify&ref=Simplify) |
| Wex | Intern - Software Engineer - Undergraduate Students Only | Remote in USA | 09/30/2025 | [APPLY](https://wexinc.wd5.myworkdayjobs.com/en-US/WEXInc/job/US---Remote/Intern---Software-Engineer--Undergraduate-Students-Only-_R19201?utm_source=Simplify&ref=Simplify) |
| RTX | Software Engineer Intern - Missile Defense Sensors | Burlington, MA | 09/29/2025 | [APPLY](https://globalhr.wd5.myworkdayjobs.com/rec_rtx_ext_gateway/job/MA311-Woburn-MA-225-Presidential-225-Presidential-Way-Goddard-Building-27-Woburn-MA-01801-USA/XMLNAME-2026-Intern---Raytheon-Missile-Defense-Sensors-Software--Engineer-Intern--On-site-_01794116?utm_source=Simplify&ref=Simplify) |
| Research Innovations | Software Engineering Internship Summer 2026 - EC2117 | Remote | 09/26/2025 | [APPLY](https://www.researchinnovations.com/) |
| General Dynamics Mission Systems | Software Engineer Intern | Pittsfield, MA | 09/26/2025 | [APPLY](https://careers-gdms.icims.com/jobs/68043/job?mobile=true&needsRedirect=false&utm_source=github-vansh-ouckah) |
| Fiber | Software Engineer Internship | Remote | 09/26/2025 | [APPLY](https://www.getfiber.ai/careers?gh_jid=4918711007&utm_source=github-vansh-ouckah) |
| State Street | BestX AI Engineer – Co-Op - Global Technology Services | Quincy, MA | 09/26/2025 | [APPLY](https://statestreet.wd1.myworkdayjobs.com/en-US/Global/job/Quincy-Massachusetts/BestX-AI-Engineer--CO-OP_R-778313?utm_source=Simplify&ref=Simplify) |
| OnePay | Software Engineer - Intern | Remote | 09/25/2025 | [APPLY](https://www.onepay.com/) |
| State Street | Data Analytics Co-Op - Databricks & Cloud | Quincy, MA | 09/25/2025 | [APPLY](https://statestreet.wd1.myworkdayjobs.com/en-US/Global/job/Quincy-Massachusetts/Data-Analytics--Databricks---Cloud--Co-Op_R-778305?utm_source=Simplify&ref=Simplify) |
| Fresenius Medical Care | Software Engineering Intern/Co-op - Multiple Teams | Andover, MA | 09/25/2025 | [APPLY](https://freseniusmedicalcare.wd3.myworkdayjobs.com/fme/job/Lawrence-MA-USA/Software-Engineering-Co-op_R0222624?utm_source=Simplify&ref=Simplify) |
| State Street | Electronic Trading Platform Software Engineer Co-Op - Global Technology Services | Quincy, MA | 09/25/2025 | [APPLY](https://statestreet.wd1.myworkdayjobs.com/en-US/Global/job/Quincy-Massachusetts/Electronic-Trading-Platform-Software-Engineer--CO-OP_R-778314?utm_source=Simplify&ref=Simplify) |
| Bracebridge Capital | Northeastern University Software Engineer - Application Development Co-op | Boston, MA | 09/24/2025 | [APPLY](https://www.bracebridgecapital.com/) |
| Bracebridge Capital | Northeastern University Software Engineer - Business Intelligence Co-op | Boston | 09/24/2025 | [APPLY](https://www.bracebridgecapital.com/) |
| SICK | Software Engineer Intern, AI/ML | Boston, MA Canton, MA | 09/24/2025 | [APPLY](https://jobs.sick.com/usa/job/Canton-Software-Engineering-Internship-(AIML)-MA-02021/37406-en_US/?utm_source=github-vansh-ouckah) |
| Sanofi | Global MSAT Automation Engineer Intern | Framingham, MA | 09/24/2025 | [APPLY](https://jobs.sanofi.com/en/job/-/-/2649/29541565056?utm_source=github-vansh-ouckah) |
| Pinterest | Software Engineer Intern | Remote US | 09/24/2025 | [APPLY](https://www.pinterestcareers.com/jobs/7202269/software-engineer-intern-2026-remote-us/?utm_source=github-vansh-ouckah) |
| Klaviyo | AI Engineer Intern | Boston, MA | 09/24/2025 | [APPLY](https://job-boards.greenhouse.io/klaviyocampus/jobs/7418442003?utm_source=github-vansh-ouckah) |
| Bracebridge Capital | Software Engineer Co-op | Boston, MA | 09/24/2025 | [APPLY](https://job-boards.greenhouse.io/bracebridgecapital/jobs/4601209005?utm_source=github-vansh-ouckah) |
| Boston Scientific | Software Development Engineer Intern | Waltham, MA | 09/24/2025 | [APPLY](https://bostonscientific.eightfold.ai/careers/job/563602808714251?utm_source=github-vansh-ouckah) |
| Accenture | Technology Analyst | Boston, MA | 09/24/2025 | [APPLY](https://www.accenture.com/us-en/careers/jobdetails?id=R00285547_en&title=Technology+Summer+Analyst+-+NAELFY26&utm_source=Simplify&ref=Simplify) |
| Hewlett Packard Enterprise | HPC/AI Software Engineering Intern - Multiple Teams | Andover, MA | 09/24/2025 | [APPLY](https://hpe.wd5.myworkdayjobs.com/Jobsathpe/job/San-Jose-California-United-States-of-America/HPC-AI-Software-Engineering-Intern_1192979?utm_source=Simplify&ref=Simplify) |
| The Bank of New York Mellon | Business Operations Intern/Co-op - Product and Innovation | Boston, MA | 09/24/2025 | [APPLY](https://bnymellon.eightfold.ai/careers/job/38082813?utm_source=Simplify&ref=Simplify) |
| State Street | Data Engineer - Co-Op - Global Technology Services | Quincy, MA | 09/24/2025 | [APPLY](https://statestreet.wd1.myworkdayjobs.com/en-US/Global/job/Quincy-Massachusetts/Data-Engineer--CO-OP_R-778223?utm_source=Simplify&ref=Simplify) |
| State Street | Data Engineer – Co-Op | Quincy, MA | 09/24/2025 | [APPLY](https://statestreet.wd1.myworkdayjobs.com/en-US/Global/job/Quincy-Massachusetts/Data-Engineer--CO-OP_R-778221?utm_source=Simplify&ref=Simplify) |
| Zillow | AI Applied Scientist - PhD Intern - Evaluation Systems and Metrics | Remote in USA | 09/24/2025 | [APPLY](https://zillow.wd5.myworkdayjobs.com/en-US/Zillow_Group_External/job/Remote-USA/AI-Applied-Scientist---PhD-Intern--Evaluation-Systems-and-Metrics_P748040?utm_source=Simplify&ref=Simplify) |
| Klaviyo | Machine Learning Engineer Intern - Multiple Teams | Boston, MA | 09/24/2025 | [APPLY](https://job-boards.greenhouse.io/klaviyocampus/jobs/7418443003?utm_source=Simplify&ref=Simplify) |
| Zillow | AI Applied Scientist Intern - Foundational IQ | Remote in USA | 09/24/2025 | [APPLY](https://zillow.wd5.myworkdayjobs.com/en-US/Zillow_Group_External/job/Remote-USA/AI-Applied-Scientist---PhD-Intern--Foundational-IQ_P748042?utm_source=Simplify&ref=Simplify) |
| Autodesk | Intern – Construction AI Agent Research | Boston | 09/24/2025 | [APPLY](https://autodesk.wd1.myworkdayjobs.com/Ext/job/Boston-MA-USA/Intern--Construction-AI-Agent-Research_25WD91971-1?utm_source=Simplify&ref=Simplify) |
| State Street | Enterprise Reference Data Analyst Co-Op - Global Technology Services | Quincy, MA | 09/24/2025 | [APPLY](https://statestreet.wd1.myworkdayjobs.com/en-US/Global/job/Quincy-Massachusetts/Enterprise-Reference-Data-Analyst--CO-OP_R-778189?utm_source=Simplify&ref=Simplify) |
| Sanofi | Intern - Global Manufacturing, Science & Technology | Framingham, MA | 09/24/2025 | [APPLY](https://sanofi.wd3.myworkdayjobs.com/en-US/SanofiCareers/job/Framingham-MA/Summer-2026-Intern----Global-MSAT-Automation-Engineer_R2803155?utm_source=Simplify&ref=Simplify) |
| Zillow | AI Applied Scientist Intern - Foundational AQ & EQ | Remote in USA | 09/24/2025 | [APPLY](https://zillow.wd5.myworkdayjobs.com/en-US/Zillow_Group_External/job/Remote-USA/AI-Applied-Scientist---PhD-Intern--Foundational-AQ---EQ_P748041?utm_source=Simplify&ref=Simplify) |
| Klaviyo | AI Engineer Intern - Multiple Teams | Boston, MA | 09/24/2025 | [APPLY](https://job-boards.greenhouse.io/klaviyocampus/jobs/7418442003?utm_source=Simplify&ref=Simplify) |
| General Dynamics Mission Systems | Software Intern Engineer | Pittsfield, MA | 09/24/2025 | [APPLY](https://careers-gdms.icims.com/jobs/68043/job?mobile=true&needsRedirect=false&utm_source=Simplify&ref=Simplify) |
| Autodesk | Intern – Software Engineer - Simulation & AI | Boston, MA | 09/24/2025 | [APPLY](https://autodesk.wd1.myworkdayjobs.com/Ext/job/Novi-MI-USA/Intern-DM---US---May-Aug-1_25WD91312-2?utm_source=Simplify&ref=Simplify) |
| Bracebridge Capital | Software Engineer Co-op - Business Intelligence | Boston, MA | 09/24/2025 | [APPLY](https://job-boards.greenhouse.io/bracebridgecapital/jobs/4601209005?utm_source=Simplify&ref=Simplify) |
| State Street | Enterprise Reference Data Analyst Co-Op | Quincy, MA | 09/23/2025 | [APPLY](https://statestreet.wd1.myworkdayjobs.com/en-US/Global/job/Quincy-Massachusetts/Enterprise-Reference-Data-Analyst--CO-OP_R-778189?utm_source=github-vansh-ouckah) |
| Klaviyo | Machine Learning Engineer Intern | Boston, MA | 09/23/2025 | [APPLY](https://job-boards.greenhouse.io/klaviyocampus/jobs/7418443003?utm_source=github-vansh-ouckah) |
| Accenture | Technology Summer Analyst Intern | TX Boston | 09/23/2025 | [APPLY](https://www.accenture.com/us-en/careers/jobdetails?id=R00285547_en&title=Technology+Summer+Analyst+-+NAELFY26&utm_source=github-vansh-ouckah) |
| SharkNinja | Spring 2026: Retail Excellence Systems & Analytics Co-op - January through June | Needham, MA | 09/23/2025 | [APPLY](https://job-boards.greenhouse.io/sharkninjaoperatingllc/jobs/4595872006?utm_source=Simplify&ref=Simplify) |
| Fidelity Investments | Undergraduate Internship - Technology | Boston, MA | 09/23/2025 | [APPLY](https://fmr.wd1.myworkdayjobs.com/fidelitycareers/job/One-Destiny-Way-Westlake-TX/Summer-2026-Undergraduate-Internship---Technology_2118142-1?utm_source=Simplify&ref=Simplify) |
| State Street | Product Management Support Co-Op - Global Technology Services | Quincy, MA | 09/23/2025 | [APPLY](https://statestreet.wd1.myworkdayjobs.com/en-US/Global/job/Quincy-Massachusetts/Product-Management-Support--CO-OP_R-778179-4?utm_source=Simplify&ref=Simplify) |
| State Street | Data Engineer - Co-Op | Quincy, MA | 09/23/2025 | [APPLY](https://statestreet.wd1.myworkdayjobs.com/en-US/Global/job/Quincy-Massachusetts/Data-Engineer--CO-OP_R-778195?utm_source=Simplify&ref=Simplify) |
| State Street | Data Governance Analyst Intern/Co-op - Data Governance - Global Technology Services | Quincy, MA | 09/23/2025 | [APPLY](https://statestreet.wd1.myworkdayjobs.com/en-US/Global/job/Quincy-Massachusetts/Data-Governance-Analyst--CO-OP_R-778183?utm_source=Simplify&ref=Simplify) |
| Lendbuzz | Machine Learning Intern - Language Understanding - Semantic Analysis | Boston, MA | 09/23/2025 | [APPLY](https://jobs.lever.co/lendbuzz/b10f1a92-80a1-438d-89b8-079de2386e74/apply?utm_source=Simplify&ref=Simplify) |
| Manulife Financial | Business Operations Intern/Co-op - Data Science | Boston, MA | 09/23/2025 | [APPLY](https://manulife.wd3.myworkdayjobs.com/en-US/MFCJH_Jobs/job/Boston-Massachusetts/Summer-Intern-Co-op-2026---Data-Science_JR25081658?utm_source=Simplify&ref=Simplify) |
| State Street | Data Governance Analyst Intern/Co-op - Data Governance - Global Technology Services | Quincy, MA | 09/23/2025 | [APPLY](https://statestreet.wd1.myworkdayjobs.com/en-US/Global/job/Quincy-Massachusetts/Data-Governance-Analyst--CO-OP_R-778182-1?utm_source=Simplify&ref=Simplify) |
| GE Vernova | Sustainability AI Solutions Intern - Multiple Teams | Cambridge, MA | 09/23/2025 | [APPLY](https://gevernova.wd5.myworkdayjobs.com/only_confidential_executive_recruiting/job/Cambridge/GE-Vernova-Sustainability-AI-Solutions-Intern---Summer-2026_R5020616?utm_source=Simplify&ref=Simplify) |
| State Street | Application Developer – Co-Op | Quincy, MA | 09/23/2025 | [APPLY](https://statestreet.wd1.myworkdayjobs.com/en-US/Global/job/Quincy-Massachusetts/Application-Developer--CO-OP_R-778177?utm_source=Simplify&ref=Simplify) |
| Peapod Digital Labs | Fulfillment Software Engineer Co-op - Fall 2026 | Quincy, MA | 09/22/2025 | [APPLY](https://www.peapoddigitallabs.com) |
| Peapod Digital Labs | Software Engineer Co-op - Fall 2026 | Quincy, MA | 09/22/2025 | [APPLY](https://www.peapoddigitallabs.com) |
| Dexcom | Intern I - DevOps Engineering | Remote in USA | 09/22/2025 | [APPLY](https://careers.dexcom.com/careers/job/38039370?utm_source=Simplify&ref=Simplify) |
| Sensata | IT Intern - AI/ML | Attleboro, MA | 09/20/2025 | [APPLY](https://sensata.wd1.myworkdayjobs.com/en-US/Sensata-Careers/job/Attleboro-Massachusetts/IT--AI-ML--Intern---Summer-2026_IRC96039?utm_source=Simplify&ref=Simplify) |
| Dexcom Corporation | DevOps Engineering Intern, I | Remote | 09/19/2025 | [APPLY](https://careers.dexcom.com/careers/job/38039370?utm_source=github-vansh-ouckah) |
| Comcast | Site Reliability Engineering Intern | Remote, US | 09/19/2025 | [APPLY](https://jobs.comcast.com/job/-/-/45483/86254804448?utm_source=github-vansh-ouckah) |
| Arm Limited | Software Engineer | Boston, MA | 09/19/2025 | [APPLY](https://careers.arm.com/job/austin/intern-software-engineer/33099/85831486384?utm_source=Simplify&ref=Simplify) |
| Block | Software Engineer Intern | CARemote in USASt. Louis, MO | 09/19/2025 | [APPLY](http://block.xyz/careers/jobs/4904196008?gh_jid=4904196008&utm_source=Simplify&ref=Simplify) |
| IBM | Back End Developer Intern | Lowell, MA, Statewide, MA | 09/19/2025 | [APPLY](https://ibmglobal.avature.net/en_US/careers/JobDetail?jobId=55372&utm_source=Simplify&ref=Simplify) |
| Google | Research Intern | Cambridge, MA | 09/19/2025 | [APPLY](https://www.google.com/about/careers/applications/jobs/results/100216277234000582-research-intern-phd-summer-2026?utm_source=Simplify&ref=Simplify) |
| Adobe | AI/ML Intern - Machine Learning Engineer | Waltham, MA | 09/19/2025 | [APPLY](https://careers.adobe.com/us/en/job/R158493/2026-AI-ML-Intern-Machine-Learning-Engineer?utm_source=Simplify&ref=Simplify) |
| Databricks | Product Design Intern | Remote | 09/19/2025 | [APPLY](https://www.databricks.com/company/careers/product/product-design-intern-8143588002?utm_source=Simplify&ref=Simplify) |
| Comcast | Comcast Data Science Intern | Remote in USA | 09/19/2025 | [APPLY](https://comcast.wd5.myworkdayjobs.com/Comcast_Careers/job/Virtual/Comcast-Data-Science-Intern_R419150?utm_source=Simplify&ref=Simplify) |
| Cotiviti | Intern – Generative AI Research Engineer | Remote in USA | 09/19/2025 | [APPLY](https://careers-cotiviti.icims.com/jobs/15661/job?mobile=true&needsRedirect=false&utm_source=Simplify&ref=Simplify) |
| Citizens Financial Group | Data Analytics Graduate Internship | Norwood, MA | 09/19/2025 | [APPLY](https://hcgn.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/jobs/job/41914?utm_source=Simplify&ref=Simplify) |
| Citizens Financial Group | Data Management Graduate Internship | Norwood, MA | 09/19/2025 | [APPLY](https://hcgn.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/jobs/job/41915?utm_source=Simplify&ref=Simplify) |
| Citizens Financial Group | Data Science Undergraduate Internship | Norwood, MA | 09/19/2025 | [APPLY](https://hcgn.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/jobs/job/41920?utm_source=Simplify&ref=Simplify) |
| Citizens Financial Group | Data Engineer Internship | Norwood, MA | 09/19/2025 | [APPLY](https://hcgn.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/jobs/job/41933?utm_source=Simplify&ref=Simplify) |
| Citizens Financial Group | Data Management Undergraduate Internship | Norwood, MA | 09/19/2025 | [APPLY](https://hcgn.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/jobs/job/41924?utm_source=Simplify&ref=Simplify) |
| Terex | IT Business Support Co-op | Quincy, WA | 09/19/2025 | [APPLY](https://terex.wd1.myworkdayjobs.com/terexcareers/job/USA-WA-Bothell/XMLNAME-2026-IT-Business-Support-Co-op_REQ-10076?utm_source=Simplify&ref=Simplify) |
| Inventing for Life | Future Talent Program – Co-Op - Chemical Biology Proteomics Data Analysis | Cambridge, MA | 09/19/2025 | [APPLY](https://msd.wd5.myworkdayjobs.com/searchjobs/job/USA---Massachusetts---Cambridge-320-Bent-Street/XMLNAME-2026-Future-Talent-Program---Chemical-Biology-Proteomics-Data-Analysis---Co-Op_R363203?utm_source=Simplify&ref=Simplify) |
| Adobe | 2026 Intern - Research Scientist/Engineer | Cambridge, MA | 09/19/2025 | [APPLY](https://adobe.wd5.myworkdayjobs.com/external_experienced/job/San-Jose/XMLNAME-2026-Intern---Research-Scientist-Engineer_R160317?utm_source=Simplify&ref=Simplify) |
| Johnson & Johnson | Production Data Analyst Co-op | Peabody, MA | 09/19/2025 | [APPLY](https://jj.wd5.myworkdayjobs.com/JJ/job/Danvers-Massachusetts-United-States-of-America/Production-Data-Analyst-Co-op_R-030501?utm_source=Simplify&ref=Simplify) |
| Moderna | 2026 Co-Op - Data Management & Clinical Data Standards | Cambridge, MA | 09/19/2025 | [APPLY](https://modernatx.wd1.myworkdayjobs.com/en-US/M_tx/job/Cambridge-Massachusetts/XMLNAME-2026-Co-Op--Data-Management---Clinical-Data-Standards_R18328-1?utm_source=Simplify&ref=Simplify) |
| Verizon Communications | Wireless Network Field Operations Internship | Boston, MA | 09/19/2025 | [APPLY](https://verizon.wd12.myworkdayjobs.com/verizon-careers/job/100-Causeway-St-Boston-MA-MA0383/Wireless-Network-Field-Operations-Summer-2026-Internship_R-1085462?utm_source=Simplify&ref=Simplify) |
| Marvell | Design for Test Engineering Intern | Westborough, MA | 09/18/2025 | [APPLY](https://marvell.wd1.myworkdayjobs.com/MarvellCareers/job/Westborough-MA/Design-for-Test-Engineering-Intern---Bachelors-Degree_2502682-1?utm_source=Simplify&ref=Simplify) |
| L3Harris Technologies | Software Engineering Intern | Burlington, MA | 09/18/2025 | [APPLY](https://jobs.l3harris.com/job/Wilmington-Software-Engineering-Intern-(Wilmington,-MA)-MA-01887/1327045300/?ats=successfactors&utm_source=Simplify&ref=Simplify) |
| Litify | Software Engineer Co-op - Cooperative Education | Remote in USA | 09/18/2025 | [APPLY](https://job-boards.greenhouse.io/litify/jobs/7257813?utm_source=Simplify&ref=Simplify) |
| Johnson & Johnson | Software Design Quality Engineer Co-op | Massachusetts | 09/17/2025 | [APPLY](https://www.jnj.com) |
| SharkNinja | Product Development Intern - Shark | Needham, MA | 09/17/2025 | [APPLY](https://job-boards.greenhouse.io/sharkninjaoperatingllc/jobs/4601627006?utm_source=Simplify&ref=Simplify) |
| Insulet Corporation | Co-op – Product Management and Design | Acton, MA | 09/17/2025 | [APPLY](https://insulet.wd5.myworkdayjobs.com/insuletcareers/job/Acton-Massachusetts/Co-op--Product-Management-and-Design--January-June-2026--Hybrid-_REQ-2025-12844?utm_source=Simplify&ref=Simplify) |
| Force Factor | Product Development Intern | Boston, MA | 09/17/2025 | [APPLY](https://forcefactor.com/pages/job-openings?gh_jid=5631124004&utm_source=Simplify&ref=Simplify) |
| SharkNinja | NPD Commercial Readiness Co-op | Needham, MA | 09/17/2025 | [APPLY](https://job-boards.greenhouse.io/sharkninjaoperatingllc/jobs/4592674006?utm_source=Simplify&ref=Simplify) |
| SharkNinja | Product Development Co-op - Ninja | Needham, MA | 09/17/2025 | [APPLY](https://job-boards.greenhouse.io/sharkninjaoperatingllc/jobs/4592274006?utm_source=Simplify&ref=Simplify) |
| SharkNinja | Data Engineering Intern | Needham, MA | 09/17/2025 | [APPLY](https://job-boards.greenhouse.io/sharkninjaoperatingllc/jobs/4601703006?utm_source=Simplify&ref=Simplify) |
| Voya Financial | Technology Intern | Remote in USA | 09/17/2025 | [APPLY](https://godirect.wd5.myworkdayjobs.com/voya_jobs/job/United-States-Remote/Summer-2026-Technology-Intern_JR0031730?utm_source=Simplify&ref=Simplify) |
| Chainlink Labs | Research Internship | Remote in USA | 09/17/2025 | [APPLY](https://jobs.ashbyhq.com/chainlink-labs/c71ed144-8eb4-4acf-9bf3-137b1b067ed8/application?utm_source=Simplify&ref=Simplify) |
| Waters | Research Machine Learning Co-op | Milford, MA | 09/17/2025 | [APPLY](https://uscareers-waters.icims.com/jobs/24104/2025-24104/job?utm_source=Simplify&ref=Simplify) |
| CAI | Data Analyst Intern | Remote in USA | 09/17/2025 | [APPLY](https://cai.wd5.myworkdayjobs.com/computer_aid/job/PA-CLIENT-STATE/Data-Analyst-Intern_R6104?utm_source=Simplify&ref=Simplify) |
| Wellington Management | Technology Undergraduate Summer Internship | Boston, MA | 09/17/2025 | [APPLY](https://wellington.wd5.myworkdayjobs.com/Campus/job/Boston-MA-United-States/Technology-Undergraduate-Summer-Internship_R92835?utm_source=Simplify&ref=Simplify) |
| Entegris | Supply Chain Data Management Co-Op | Bedford, MA | 09/17/2025 | [APPLY](https://entegris.wd1.myworkdayjobs.com/entegriscareers/job/Bedford-MA/Supply-Chain-Data-Management-Co-Op---Spring-2026_REQ-9155?utm_source=Simplify&ref=Simplify) |
| Merck | 2026 Future Talent Program – Co-op - Data Scientist - Causal Network | Cambridge, MA | 09/17/2025 | [APPLY](https://msd.wd5.myworkdayjobs.com/searchjobs/job/USA---Massachusetts---Cambridge-320-Bent-Street/XMLNAME-2026-Future-Talent-Program---Data-Scientist--Causal-Network---Co-op_R364594?utm_source=Simplify&ref=Simplify) |
| L3Harris Technologies | Field Eng Intern | Fall River, MA | 09/17/2025 | [APPLY](https://jobs.l3harris.com/job/Fall-River-Field-Eng-Intern-(Fall-River,-MA)-MA-02723/1324524600/?ats=successfactors&utm_source=Simplify&ref=Simplify) |
| Santander Global Facilities (SGF) US - Santander Group | Technology & Data Analytics Intern | Quincy, MA | 09/17/2025 | [APPLY](https://santander.wd3.myworkdayjobs.com/santandercareers/job/1-Enterprise-Drive-Quincy-Corp/Technology---Data-Analytics-Intern_Req1489885?utm_source=Simplify&ref=Simplify) |
| Thermo Fisher Scientific | IT Services & Delivery Intern | Waltham | 09/17/2025 | [APPLY](https://thermofisher.wd5.myworkdayjobs.com/ThermoFisherCareers/job/Waltham-Massachusetts-USA/IT-Services---Delivery-Intern_R-01328653?utm_source=Simplify&ref=Simplify) |
| Thermo Fisher Scientific | Sr. Sales Technology – Intern - AI Innovation | Waltham, MA | 09/17/2025 | [APPLY](https://thermofisher.wd5.myworkdayjobs.com/ThermoFisherCareers/job/Waltham-Massachusetts-USA/Sr-Sales-Technology--AI-Innovation--Intern_R-01328124?utm_source=Simplify&ref=Simplify) |
| Ernst & Young | Intern - Tax - Itts - Transaction Tax Advisory - Jd LLM - Summer 2026 | Boston, MA | 09/17/2025 | [APPLY](https://eyglobal.yello.co/jobs/Vn0auTRiuN4HgdckGhrUZA?job_board_id=c1riT--B2O-KySgYWsZO1Q&utm_source=Simplify&ref=Simplify) |
| Kensho | Machine Learning Intern | Cambridge | 09/17/2025 | [APPLY](https://spgi.wd5.myworkdayjobs.com/en-US/kensho_careers/job/New-York-NY/Machine-Learning-Intern---Summer-2026_319677-1?utm_source=Simplify&ref=Simplify) |
| MSD | 2026 Future Talent Program – Intern - Nonclinical Drug Safety Data Scientist | Boston, MA | 09/17/2025 | [APPLY](https://msd.wd5.myworkdayjobs.com/en-US/SearchJobs/job/USA---Pennsylvania---West-Point/XMLNAME-2026-Future-Talent-Program---Nonclinical-Drug-Safety-Data-Scientist---Intern_R362142?utm_source=Simplify&ref=Simplify) |
| S&P Global | Machine Learning Intern | Cambridge, MA | 09/17/2025 | [APPLY](https://spgi.wd5.myworkdayjobs.com/en-US/SPGI_Careers/job/New-York-NY/Machine-Learning-Intern---Summer-2026_319677?utm_source=Simplify&ref=Simplify) |
| Seagate Technology | Agentic Data Analyst Intern - Global Revenue Operations | Remote in USALongmont, CO | 09/17/2025 | [APPLY](https://seagatecareers.com/job/Agentic-Data-Analyst-Intern-Global-Revenue-Operations/1323169900/?ats=successfactors&utm_source=Simplify&ref=Simplify) |
| Varian | Software & Data Science Internships | Remote in USA | 09/17/2025 | [APPLY](https://onehealthineers.wd3.myworkdayjobs.com/SHSJB/job/CYA-G/XMLNAME-2026-Software---Data-Science-Internships_R-23658?utm_source=Simplify&ref=Simplify) |
| Moderna | Applied Technologies Intern - Technical Development | Norwood, MA | 09/17/2025 | [APPLY](https://modernatx.wd1.myworkdayjobs.com/en-US/M_tx/job/Norwood-Massachusetts/XMLNAME-2026-Applied-Technologies-Intern--Technical-Development_R18217?utm_source=Simplify&ref=Simplify) |
| Amgen | Grad Intern - Amgen Technology & Medical Organizations | Remote in USA | 09/17/2025 | [APPLY](https://amgen.wd1.myworkdayjobs.com/careers/job/United-States---Remote/Grad-Intern---Amgen-Technology---Medical-Organizations--Summer-2026-_R-224644?utm_source=Simplify&ref=Simplify) |
| Amgen | Undergrad Intern - Amgen Technology & Medical Organizations | Remote in USA | 09/17/2025 | [APPLY](https://amgen.wd1.myworkdayjobs.com/careers/job/United-States---Remote/Undergrad-Intern---Amgen-Technology---Medical-Organizations--Summer-2026-_R-224647?utm_source=Simplify&ref=Simplify) |
| Takeda | Analytics Leadership Development Program Summer Internship | Boston, MA | 09/17/2025 | [APPLY](https://takeda.wd3.myworkdayjobs.com/external/job/Boston-MA/Analytics-Leadership-Development-Program-Summer-Internship_R0162008?utm_source=Simplify&ref=Simplify) |
| L3Harris Technologies | Field Engineer Intern | Fall River, MA | 09/17/2025 | [APPLY](https://jobs.l3harris.com/job/Fall-River-Field-Engineer-Intern-(Fall-River,-MA)-MA-02723/1321600200/?ats=successfactors&utm_source=Simplify&ref=Simplify) |
| Santander | Salesforce and Data Engineering Intern | Boston, MA | 09/17/2025 | [APPLY](https://santander.wd3.myworkdayjobs.com/SantanderCareers/job/Boston/Salesforce-and-Data-Engineering-Intern_Req1487884?utm_source=Simplify&ref=Simplify) |
| Marmon Holdings | AI Coding & Process Intern | Remote in USA | 09/17/2025 | [APPLY](https://marmon.wd501.myworkdayjobs.com/en-US/Marmon_Careers/job/Remote---United-States-of-America/AI-Coding---Process-Intern_JR0000036525-2?utm_source=Simplify&ref=Simplify) |
| Santander | Model Development Intern | Boston, MA | 09/17/2025 | [APPLY](https://santander.wd3.myworkdayjobs.com/SantanderCareers/job/Boston/Model-Development-Intern_Req1486222-2?utm_source=Simplify&ref=Simplify) |
| Analog Devices | Algorithm Engineer Intern | Boston, MA | 09/17/2025 | [APPLY](https://analogdevices.wd1.myworkdayjobs.com/en-US/External/job/US-MA-Wilmington/Algorithm-Engineer-Intern_R255043?utm_source=Simplify&ref=Simplify) |
| Skyworks | AI Engineering Summer/Fall Co-Op | Burlington, MA | 09/17/2025 | [APPLY](https://careers.skyworksinc.com/job/Woburn-AI-Engineering-SummerFall-Co-Op-(June-'26-Dec-'26)-MA-01801/1319302300/?ats=successfactors&utm_source=Simplify&ref=Simplify) |
| Acadian Asset Management | Quantitative Research Intern | Boston, MA | 09/17/2025 | [APPLY](https://www.acadian-asset.com/careers/open-positions?gh_jid=4600563006&utm_source=Simplify&ref=Simplify) |
| Arrowstreet Capital | Investment Processes Intern | Boston, MA | 09/17/2025 | [APPLY](https://arrowstreetcapital.wd5.myworkdayjobs.com/en-US/Campus_Careers/job/Boston/Investment-Processes-Intern--Summer-2026_R1355?utm_source=Simplify&ref=Simplify) |
| Arrowstreet Capital | Quantitative Developer Intern | Boston, MA | 09/17/2025 | [APPLY](https://arrowstreetcapital.wd5.myworkdayjobs.com/en-US/Arrowstreet/job/Boston/Quantitative-Developer-Intern--Summer-2026_R1338-1?utm_source=Simplify&ref=Simplify) |
| ZOLL Medical Corporation | Test Development Engineering Co-Op | Lowell, MA | 09/17/2025 | [APPLY](https://zoll.wd5.myworkdayjobs.com/en-US/ZOLLMedicalCorp/job/Chelmsford-MA/Test-Development-Engineering-Co-Op_R16632?utm_source=Simplify&ref=Simplify) |
| MKS Instruments | Embedded Software Engineer Co-op | Andover, MA | 09/17/2025 | [APPLY](https://mksinst.wd1.myworkdayjobs.com/en-US/MKSCareersUniversity/job/Andover-MA/XMLNAME-2026-Summer-and-Fall-Embedded-Software-Engineer-Co-op_R14749?utm_source=Simplify&ref=Simplify) |
| Voyant Photonics | Internship - Lidar Test Engineering | Lawrence, MA | 09/17/2025 | [APPLY](https://jobs.ashbyhq.com/voyant-photonics/2b39c5b6-4ef5-4891-8ae9-65c21b10769f/application?utm_source=Simplify&ref=Simplify) |
| Analog Devices | Product Engineer Prod Dev Intern | Burlington, MA | 09/17/2025 | [APPLY](https://analogdevices.wd1.myworkdayjobs.com/en-US/External/job/US-MA-Wilmington/Product-Engineer-Prod-Dev-Intern_R255239?utm_source=Simplify&ref=Simplify) |
| Dexcom | Software Test Engineering | Remote in USA | 09/17/2025 | [APPLY](https://dexcom.wd1.myworkdayjobs.com/en-US/dexcom/job/Remote---United-States/Intern-I---Software-Test-Engineering_JR114243?utm_source=Simplify&ref=Simplify) |
| Dexcom | Intern I – Software Development Engineering | Remote in USA | 09/17/2025 | [APPLY](https://dexcom.wd1.myworkdayjobs.com/Dexcom/job/Remote---United-States/Intern-I---Software-Development-Engineering_JR114292?utm_source=Simplify&ref=Simplify) |
| SharkNinja | Digital & Website Technology Intern | Needham, MA | 09/17/2025 | [APPLY](https://job-boards.greenhouse.io/sharkninjaoperatingllc/jobs/4601472006?utm_source=Simplify&ref=Simplify) |
| SharkNinja | Mobile App Developer Intern | Needham, MA | 09/17/2025 | [APPLY](https://job-boards.greenhouse.io/sharkninjaoperatingllc/jobs/4601474006?utm_source=Simplify&ref=Simplify) |
| Babel Street | Software Engineer Co-op - Text Analytics | Somerville, MA | 09/17/2025 | [APPLY](https://job-boards.greenhouse.io/babelstreet/jobs/7248507?utm_source=Simplify&ref=Simplify) |
| Dexcom | SW Development Engineering | Remote in USA | 09/17/2025 | [APPLY](https://careers.dexcom.com/careers/job/37990370?utm_source=Simplify&ref=Simplify) |
| FactSet | Software Engineer Intern | Boston, MA | 09/17/2025 | [APPLY](https://factset.wd108.myworkdayjobs.com/FactSetCareers/job/Norwalk-CT-USA/Software-Engineer-Intern---Americas-Campus--Summer-2026-_R29383?utm_source=Simplify&ref=Simplify) |
| Dexcom | Intern I – IT Integrations | Remote in USA | 09/17/2025 | [APPLY](https://dexcom.wd1.myworkdayjobs.com/Dexcom/job/Remote---United-States/Intern-I---IT-Integrations_JR114279?utm_source=Simplify&ref=Simplify) |
| Klaviyo | Front-end Software Engineer Intern | Boston, MA | 09/17/2025 | [APPLY](https://job-boards.greenhouse.io/klaviyocampus/jobs/7144468003?utm_source=Simplify&ref=Simplify) |
| InterSystems | Summer Internship | Boston, MA | 09/17/2025 | [APPLY](https://www.intersystems.com/careers/careers-search/?gh_jid=7241533003&utm_source=Simplify&ref=Simplify) |
| Tokyo Electron | Software Engineer Intern | Lowell, MA | 09/17/2025 | [APPLY](https://tel.wd3.myworkdayjobs.com/tel-careers/job/North-Chelmsford/Software-Engineer-Intern--Summer-2026-_R25-01190?utm_source=Simplify&ref=Simplify) |
| Fidelity | Co-op, Software Engineer | Boston, MA | 09/17/2025 | [APPLY](https://fmr.wd1.myworkdayjobs.com/en-US/targeted/job/Boston-MA/Co-op--Software-Engineer_2117625?utm_source=Simplify&ref=Simplify) |
| Red Hat | Software Engineer Intern | Boston, MA | 09/17/2025 | [APPLY](https://redhat.wd5.myworkdayjobs.com/en-US/jobs/job/Boston/Software-Engineer-Intern_R-050437?utm_source=Simplify&ref=Simplify) |
| Suno | Software Engineering Internship | Cambridge, MA | 09/17/2025 | [APPLY](https://jobs.ashbyhq.com/suno/35b8b187-b136-4bf6-af4d-b28ff892dc53/application?utm_source=Simplify&ref=Simplify) |
| Reframe Systems | Software Engineer | Andover, MA | 09/17/2025 | [APPLY](https://jobs.ashbyhq.com/reframesystems/ea0a6ec8-939f-40cb-9377-a7da31b91a53/application?utm_source=Simplify&ref=Simplify) |
| General Dynamics Mission Systems | Software Engineering Intern | Dedham, MA | 09/17/2025 | [APPLY](https://careers-gdms.icims.com/jobs/67909/job?mobile=true&needsRedirect=false&utm_source=Simplify&ref=Simplify) |
| Citizens Financial Group | Software Engineer Internship | Norwood, MA | 09/17/2025 | [APPLY](https://hcgn.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/jobs/job/41934?utm_source=Simplify&ref=Simplify) |
| Reframe Systems | Software Engineer – Full Stack Robotics Intern | Andover, MA | 09/17/2025 | [APPLY](https://jobs.ashbyhq.com/reframesystems/76b3c3d9-c741-4707-bd38-1d5e75781520/application?utm_source=Simplify&ref=Simplify) |
| Medtronic | Engineering Intern Summer 2026 | Boston, MA | 09/17/2025 | [APPLY](https://medtronic.wd1.myworkdayjobs.com/MedtronicCareers/job/Minneapolis-Minnesota-United-States-of-America/Engineering-Intern-Summer-2026---Candidates-Attending-2025--SWE-National-Convention_R44915-1?utm_source=Simplify&ref=Simplify) |
| Veeam Software | Kasten Engineering Intern | Remote in USA | 09/17/2025 | [APPLY](https://job-boards.eu.greenhouse.io/veeamsoftware/jobs/4650993101?utm_source=Simplify&ref=Simplify) |
| Manulife Financial | Summer Intern/Co-op - Software Engineering | Boston, MA | 09/17/2025 | [APPLY](https://manulife.wd3.myworkdayjobs.com/en-US/MFCJH_Jobs/job/Boston-Massachusetts/Summer-Intern-Co-op-2026---Software-Engineering_JR25081349?utm_source=Simplify&ref=Simplify) |
| Datadog | Software Engineering Intern - Summer | Boston, MA | 09/17/2025 | [APPLY](https://careers.datadoghq.com/detail/7158137/?gh_jid=7158137&utm_source=Simplify&ref=Simplify) |
| Kensho | Software Engineer Intern | Cambridge | 09/17/2025 | [APPLY](https://spgi.wd5.myworkdayjobs.com/en-US/kensho_careers/job/New-York-NY/Software-Engineer-Intern---Summer-2026_319680-1?utm_source=Simplify&ref=Simplify) |
| Santander Global Facilities (SGF) US - Santander Group | Payments Technology Intern | Quincy, MA | 09/17/2025 | [APPLY](https://santander.wd3.myworkdayjobs.com/santandercareers/job/1-Enterprise-Drive-Quincy-Corp/Payments-Technology-Intern_Req1488422?utm_source=Simplify&ref=Simplify) |
| DraftKings | Software Engineer Intern | Boston, MA | 09/17/2025 | [APPLY](https://draftkings.wd1.myworkdayjobs.com/en-US/Campus_Career_Portal/job/Boston-MA/Software-Engineer-Intern--Summer-2026-_JR12655?utm_source=Simplify&ref=Simplify) |
| The Hanover | Associate Solutions Developer | Worcester, MA | 09/17/2025 | [APPLY](https://jobs.dayforcehcm.com/en-US/thg/ALLCAREERS/jobs/38827?utm_source=Simplify&ref=Simplify) |
| Dropbox | Software Engineer Intern | Remote in USA | 09/17/2025 | [APPLY](https://boards.greenhouse.io/embed/job_app?token=7183241&utm_source=Simplify&ref=Simplify) |
| Klaviyo | Full-stack Software Engineer Intern | Boston, MA | 09/15/2025 | [APPLY](https://job-boards.greenhouse.io/klaviyocampus/jobs/7144362003?utm_source=github-vansh-ouckah) |
| ICF | Software Developer Intern | Remote | 09/15/2025 | [APPLY](https://careers.icf.com/us/en/job/IIIIIIUSR2502588EXTERNALENUS/2026-Summer-Intern-Software-Developer?utm_source=github-vansh-ouckah) |
| Dexcom | SW Development Engineering Intern | Remote | 09/15/2025 | [APPLY](https://careers.dexcom.com/careers/job/37990370?utm_source=github-vansh-ouckah) |
| Anima | Intern/New Grad Software Engineer | Remote | 09/14/2025 | [APPLY](https://www.animahealth.com/) |
| Klaviyo | Full-stack Software Engineer Intern - Summer 2026 | Boston, MA | 09/12/2025 | [APPLY](https://www.klaviyo.com/) |
| Klaviyo | Front-end Software Engineer Intern - Summer 2026 | Boston, MA | 09/12/2025 | [APPLY](https://www.klaviyo.com/) |
| Klaviyo | Front-end Software Engineer Co-op - Spring 2026 | Boston, MA | 09/12/2025 | [APPLY](https://www.klaviyo.com/) |
| Klaviyo | Full-stack Software Engineer Co-op - Spring 2026 | Boston, MA | 09/12/2025 | [APPLY](https://www.klaviyo.com/) |
| Reframe Systems | Software Engineer - Pixels-to-Parts Intern Summer 2026 | Andover, MA | 09/12/2025 | [APPLY](https://www.reframe.systems/) |
| Staples | Software Engineering Intern, SDS e-Commerce | Framingham, MA | 09/12/2025 | [APPLY](https://careers.staples.com/en/job/-/-/44412/86032290864?utm_source=github-vansh-ouckah) |
| EagleView | Software Engineer Intern | Remote US | 09/12/2025 | [APPLY](https://careers-eagleview.icims.com/jobs/2594/job?utm_source=github-vansh-ouckah) |
| Reframe Systems | Software Engineer - Full Stack Robotics Intern Summer 2026 | Andover, MA | 09/11/2025 | [APPLY](https://www.reframe.systems/) |
| Suno | Software Engineering Intern | Cambridge, MA | 09/11/2025 | [APPLY](https://jobs.ashbyhq.com/suno/35b8b187-b136-4bf6-af4d-b28ff892dc53?utm_source=github-vansh-ouckah) |
| Veeam | Integrations Software Developer Intern - Summer 2026 | Remote | 09/10/2025 | [APPLY](https://www.veeam.com/) |
| Reframe Systems | Software Engineer and Full Stack Robotics Intern | Andover, MA | 09/10/2025 | [APPLY](https://jobs.ashbyhq.com/reframesystems/76b3c3d9-c741-4707-bd38-1d5e75781520/application?utm_source=github-vansh-ouckah) |
| Citizens Financial Group | Data Engineer Intern | RI Norwood | 09/10/2025 | [APPLY](https://hcgn.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/jobs/job/41933?utm_source=github-vansh-ouckah) |
| Liberty Mutual Insurance | Solaria Labs Software Development Co-op - January - June 2026 | Boston, Massachusetts | 09/09/2025 | [APPLY](https://jobs.libertymutualgroup.com/digital-technology) |
| Suno | Software Engineering Internship - Summer 2026 | Boston | 09/09/2025 | [APPLY](https://www.suno.com/) |
| Datadog | Software Engineering Intern | Boston | 09/08/2025 | [APPLY](https://careers.datadoghq.com/detail/7158137/?utm_source=github-vansh-ouckah) |
| Arm | Software Engineer Intern | TX Boston | 09/07/2025 | [APPLY](https://careers.arm.com/job/austin/intern-software-engineer/33099/85831486384?utm_source=github-vansh-ouckah) |
| Ameritas Life Insurance Corp | Software Developer Intern, Packaged Systems | Remote | 09/07/2025 | [APPLY](https://myjobs.adp.com/ameritasexternal/cx/job-details?reqId=5001146090600&utm_source=github-vansh-ouckah) |
| MathWorks | Engineering Development Group Intern | Natick, MA | 09/02/2025 | [APPLY](https://www.mathworks.com/company/jobs/opportunities/25610-multiple-openings-engineering-development-group-internship?utm_source=github-vansh-ouckah) |
| DraftKings | Software Engineer Intern-Referral - Summer 2026 | Boston, MA | 08/30/2025 | [APPLY](https://draftkings.com/) |
| Red Hat | Software Engineer Co-op | Lowell | 08/30/2025 | [APPLY](https://www.redhat.com) |
| AMD | Software Engineer Intern | CO Boxborough , MA | 08/29/2025 | [APPLY](https://careers.amd.com/careers-home/jobs/70483?lang=en-us&utm_source=github-vansh-ouckah) |
| Upsolve | Software Engineering Intern | Remote | 08/28/2025 | [APPLY](https://www.workatastartup.com/jobs/80380?utm_source=github-vansh-ouckah) |
| Analog Devices | Embedded Software Intern | US, MA, Boston | 08/27/2025 | [APPLY](https://www.analog.com) |
| Analog Devices | Embedded Software Intern, Analog Garage PST | Boston, MA | 08/27/2025 | [APPLY](https://analogdevices.wd1.myworkdayjobs.com/en-US/External/job/US-MA-Boston/Embedded-Software-Intern_R255237?utm_source=github-vansh-ouckah) |
| The Hanover | Associate Solutions Developer Intern | Worcester, MA | 08/26/2025 | [APPLY](https://jobs.dayforcehcm.com/en-US/thg/ALLCAREERS/jobs/38827?utm_source=github-vansh-ouckah) |
| Google | Software Engineering Intern, BS | CO Cambridge | 08/25/2025 | [APPLY](https://www.google.com/about/careers/applications/jobs/results/75808725415142086-software-engineering-intern-bs-summer-2026?utm_source=github-vansh-ouckah) |
| Dropbox | Software Engineering Intern | Remote | 08/25/2025 | [APPLY](https://jobs.dropbox.com/listing/7183241/apply?utm_source=github-vansh-ouckah) |
| IBM | Software Engineer Intern | NY Lowell | 08/22/2025 | [APPLY](https://ibmglobal.avature.net/en_US/careers/JobDetail?jobId=54845&utm_source=github-vansh-ouckah) |
| Cadence Solutions | Software Engineering Intern - Summer 2026 | Remote | 08/21/2025 | [APPLY](https://www.cadence.care/) |
| Adobe | Machine Learning Engineer Intern, AI/ML | CA Waltham | 08/15/2025 | [APPLY](https://careers.adobe.com/us/en/job/ADOBUSR158493EXTERNALENUS/2026-AI-ML-Intern-Machine-Learning-Engineer?utm_source=github-vansh-ouckah) |
| Shopify | USA Engineering Internships | Remote | 08/13/2025 | [APPLY](https://www.shopify.com/careers/usa-engineering-internships-summer-2026-usa_b2dbdf1e-ab44-46ed-9a11-69a1a1e4b20c?keyword=intern&utm_source=github-vansh-ouckah) |
| Anduril Industries | Software Engineer Intern | United States Boston, Massachusetts | 08/12/2025 | [APPLY](https://www.anduril.com) |
| Oklahoma City Thunder | Software Engineer Intern, Basketball Operations | Remote | 08/12/2025 | [APPLY](https://www.paycomonline.net/v4/ats/web.php/jobs/ViewJobDetails?job=316815&clientkey=8E7F16AD6654E4ED3797EE9F40DB0A48&source=Indeed&utm_source=github-vansh-ouckah) |
| Anduril | Software Engineer Intern | GA Boston | 08/11/2025 | [APPLY](https://job-boards.greenhouse.io/andurilindustries/jobs/4807506007?gh_jid=4807506007&gh_src=&utm_source=github-vansh-ouckah) |
| Hyannis Port Research | Software Engineering Intern - Summer 2026 | Needham, MA | 08/02/2025 | [APPLY](https://hyannisportresearch.com) |
| HPR | Software Engineering Intern | Needham, MA | 08/02/2025 | [APPLY](https://job-boards.greenhouse.io/hyannisportresearch/jobs/6667961003?gh_src=9yscuffh3us&utm_source=github-vansh-ouckah) |
| Hypergiant Sensory Sciences | SkillBridge Internship - Frontend Engineer | Remote | 07/22/2025 | [APPLY](https://www.hypergiant.com) |
| Blackrock | 2026 Summer Intern | GA Boston | 03/04/2025 | [APPLY](https://blackrock.tal.net/vx/lang-en-GB/mobile-0/brand-3/xf-e774a855fe31/candidate/so/pm/1/pl/1/opp/9601-2026-Summer-Internship-Program-AMERS/en-GB?utm_source=github-vansh-ouckah) |

---

## Data Sources

This project aggregates internship listings from several sources:

1. **Company Career Pages** - Direct scraping from Greenhouse and Lever job boards
2. **Adzuna API** (optional) - Broad job search across multiple platforms
3. **GitHub Job Boards** - Curated lists from community-maintained repositories:
   - 🙏 [SimplifyJobs/Summer2026-Internships](https://github.com/SimplifyJobs/Summer2026-Internships) - Maintained by [Pitt CSC](https://pittcsc.org/) and [Simplify](https://simplify.jobs/)
   - 🙏 [speedyapply/2026-SWE-College-Jobs](https://github.com/speedyapply/2026-SWE-College-Jobs) - Comprehensive SWE internship tracker
   - 🙏 [vanshb03/Summer2026-Internships](https://github.com/vanshb03/Summer2026-Internships) - Community-driven internship list
   
   **Huge thanks to these maintainers** for their incredible work keeping these lists updated daily! Their repositories track thousands of roles across software engineering, data science, quant, and more.
4. **SERP API** (optional) - Discover new companies hiring via Google Search

**Note**: Product Management positions are excluded from GitHub sources to focus on technical roles.

---

## Setup Instructions

### Prerequisites
- Python 3.7+
- pip (Python package manager)
- Git

### Clone the Repository
```bash
git clone https://github.com/dariadobrolinski/tech-internships-boston-area
cd tech-internships-boston-area
```

### Install Dependencies
```bash
pip install requests pyyaml
```

### Configure Environment Variables
Create a `.env` file in the root directory with your API keys:
```bash
# Optional: For Adzuna job search
ADZUNA_APP_ID=your_adzuna_app_id
ADZUNA_APP_KEY=your_adzuna_app_key

# Optional: For discovering new companies via Google Search
SERPAPI_KEY=your_serpapi_key
```

**Get API Keys:**
- **Adzuna**: Sign up at [adzuna.com/developers](https://developer.adzuna.com/)
- **SERP API**: Sign up at [serpapi.com](https://serpapi.com/)

📖 **Need detailed setup instructions?** See the [API Keys Guide](docs/API_KEYS.md) for step-by-step instructions.

> Note: The script will work with just Greenhouse/Lever searches even without API keys. The API keys are optional but enable additional job sources.

### Edit Configuration
Customize `companies.yml` to add/remove companies or adjust search keywords:
```yaml
companies:
  - name: YourCompany
    provider: greenhouse  # or "lever"
    slug: yourcompany-slug
    include_keywords: []
    exclude_keywords: []
```

### Run the Script
```bash
# Make the script executable
chmod +x run_all.sh

# Run all job searches
./run_all.sh
```

This will:
1. Search Greenhouse and Lever job boards for configured companies
2. (Optional) Search Adzuna for internships in the Boston area
3. Scrape SimplifyJobs Summer2026-Internships repo for Boston/Remote positions
4. (Optional) Discover new companies via Google Search
5. Append all new results to `README.md` (automatically skips duplicates)
6. **Sort all jobs by date** (newest first) - keeps your README organized!

**Run individual scrapers:**
```bash
# Run just the SimplifyJobs scraper
./run_simplify.sh

# Run with dry-run to preview what would be added
./run_simplify.sh --dry-run

# Exclude remote positions (only show Boston area)
./run_simplify.sh --no-remote

# Run all other scrapers (excluding SimplifyJobs)
python3 scripts/job_report.py
python3 scripts/adzuna_report.py  # if API keys configured

# Manually sort README by date if needed
python3 scripts/sort_readme.py
```

**About the SimplifyJobs Scraper:**

The SimplifyJobs scraper automatically fetches the latest internship listings from the community-maintained [Summer2026-Internships](https://github.com/SimplifyJobs/Summer2026-Internships) repository and filters them for:
- Boston area locations (Boston, Cambridge, Somerville, Waltham, Burlington, Quincy, Needham, Lowell, Worcester, Newton)
- Remote positions in the US

Key features:
- ✅ Parses 2500+ tech internships daily
- ✅ Smart date parsing (handles "Oct 17", "2d ago", "1w ago" formats)
- ✅ Automatic deduplication (won't add duplicates)
- ✅ Filters out closed positions (marked with 🔒)
- ✅ Supports dry-run mode for testing

The SimplifyJobs repo is maintained by the [Pitt Computer Science Club](https://pittcsc.org/) and [Simplify](https://simplify.jobs/) with contributions from 800+ community members. It's an incredible resource that aggregates internships from across the tech industry - this scraper simply filters it for Boston/Remote opportunities!

### Job Sorting

All job listings in the README are automatically sorted by date (newest first) when you run `./run_all.sh`. This ensures the freshest opportunities are always at the top!

**Features:**
- ✅ Automatic sorting after all scrapers complete
- ✅ Newest jobs appear at the top of the table
- ✅ Manual sort available anytime: `python3 scripts/sort_readme.py`
- ✅ Works with jobs from all sources (Greenhouse, Lever, Adzuna, SimplifyJobs)

**Note:** The sort script is automatically run at the end of `run_all.sh`, but you can also run it manually if you ever need to re-organize your README.

### Customize Search Parameters
Edit `run_all.sh` to customize:
- **Keywords**: Change the search terms for Adzuna
- **Locations**: Modify Boston area cities
- **Remote jobs**: Add/remove `--include-remote` flag

### Automate with Cron (Optional)
Run daily at 9 AM:
```bash
crontab -e
# Add this line:
0 9 * * * cd ~/tech-internships-boston-area && ./run_all.sh >> ~/tech-internships-boston-area/cron.log 2>&1
```

---

**Happy job hunting! 🎉**
