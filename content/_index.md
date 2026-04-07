---
# Home-Page
title: Home
type: landing

sections:

# ======================
# TITEL IMAGE
# ======================
- block: markdown
  content:
    text: |
      <div class="hero-home">
          <img src="https://timexaigroup.github.io/TimeXAI-Hugo-Page/uploads/hero1.png" alt="Hero Image"/>
      </div>
  design:
    columns: '1'
    spacing:
      padding: ['0','0','0','0']
    css_class: hero-fullwidth

# ======================
# INTRO + ANIMATION ICONS
# ======================
- block: markdown
  content:
    text: |
      <div class="home-intro-icons text-center">
        <div class="home-intro">        
          <img src="https://timexaigroup.github.io/TimeXAI-Hugo-Page/uploads/aai_logo_2.png" alt="AAI Logo" class="intro-logo"/>
          <h1 class="text-center">Applied AI Lab</h1>
          <p class="text-center">
            The Applied Artificial Intelligence Lab, at <a href="https://www.thm.de/site/" target="_blank">Technische Hochschule Mittelhessen University of Applied Sciences</a>, within the <a href="https://www.thm.de/mnd/" target="_blank">Department of Mathematics, Natural Sciences and Data Processing</a> and the Centre of Competence for Information Technology (<a href="[https://www.thm.de/mnd/](https://www.thm.de/kompetenzzentren/en/kite)" target="_blank">KITE</a>), is headed by Prof. Dr. Jennifer Hannig, Professor of Artificial Intelligence at THM and  <a href="https://hessian.ai/" target="_blank">hessian.AI</a> (Hessian Center for Artificial Intelligence).
          </p>
        </div>
        <div class="home-about-icons">
          <div class="care-item">
            <a href="https://timexaigroup.github.io/TimeXAI-Hugo-Page/aai/" class="care-inner">
              <img src="https://timexaigroup.github.io/TimeXAI-Hugo-Page/uploads/aai_icon2.png" alt="Applied AI"/>
            </a>
          </div>
          <div class="care-item">
            <a href="https://timexaigroup.github.io/TimeXAI-Hugo-Page/research" class="care-inner">
               <img src="https://timexaigroup.github.io/TimeXAI-Hugo-Page/uploads/project_icon2.png" alt="Projects"/>
            </a>
          </div>
          <div class="care-item">
            <a href="https://timexaigroup.github.io/TimeXAI-Hugo-Page/students" class="care-inner">
              <img src="https://timexaigroup.github.io/TimeXAI-Hugo-Page/uploads/teaching_icon2.png" alt="Students"/>
            </a>
          </div>
          <div class="care-item">
            <a href="https://timexaigroup.github.io/TimeXAI-Hugo-Page/publications" class="care-inner">
              <img src="https://timexaigroup.github.io/TimeXAI-Hugo-Page/uploads/paper_icon2.png" alt="Publications"/>
            </a>
          </div>
        </div>
      </div>
  design:
    columns: '1'
    spacing:
      padding: ['80px','30px','80px','30px']

# ======================
# PARTNER LOGOS
# ======================
- block: markdown
  content:
    text: |
      <div class="hero-partner-logos text-center">
        <a href="/appliedAI/" target="_blank">
          <img src="https://timexaigroup.github.io/TimeXAI-Hugo-Page/uploads/aai_logo.png" alt="Applied AI Lab"/>
        </a>
        <a href="https://www.thm.de/kompetenzzentren/kite/profil.html" target="_blank">
         <img src="https://timexaigroup.github.io/TimeXAI-Hugo-Page/uploads/kite_logo.png" alt="KITE"/>
        </a>
        <a href="https://www.thm.de" target="_blank">
          <img src="https://timexaigroup.github.io/TimeXAI-Hugo-Page/uploads/THM_logo.png" alt="THM"/>
        </a>
        <a href="https://hessian.ai" target="_blank">
          <img src="https://timexaigroup.github.io/TimeXAI-Hugo-Page/uploads/HessenAi_logo.png" alt="HessenAI"/>
        </a>
      </div>
  design:
    columns: '1'
    spacing:
      padding: ['20px','0','70px','0']

# ======================
# LATEST NEWS
# ======================
- block: collection
  content:
    text: |
      <div class="latest-news-section">
        <h1 class="text-center">Latest News</h1>
        <p class="text-center">
          Check out the latest activities!
        </p>
      </div>
  filters:
    folders:
      - news
    order: desc
    limit: 3
  design:
    view: card
    columns: '3'
    css_id: news
    show_image: true
    show_date: true
    show_summary: true
    spacing:
      padding: ['60px','30px','60px','30px']

# ======================
# OPEN POSITIONS
# ======================
- block: markdown
  content:
    text: |
      <div class="open-positions-section">
        <h1 class="text-center">Open Positions</h1>
        <p class="text-center">
          Discover the opportunities we offer!<br>
          We are always interested in connecting with motivated and talented individuals. 
          Whether you are a student, researcher or expert, we offer you to collaborate on projects and contribute your expertise.       
          Join our team and help us to further develop research in the field of applied artificial intelligence!
        </p>

        <div class="home-open-positions">
          <div class="position-item">
            <a href="https://www.thm.de/site/hochschule/profil/job-und-karriere/aktuelle-stellenangebote.html" target="_blank">
              <img src="https://timexaigroup.github.io/TimeXAI-Hugo-Page/uploads/thm_job_icon.png" alt="THM Jobs"/>
            </a>         
          </div>
          <div class="position-item">
            <a href="https://timexaigroup.github.io/TimeXAI-Hugo-Page/hiwi-offers">
              <img src="https://timexaigroup.github.io/TimeXAI-Hugo-Page/uploads/hiwi_job_icon.png" alt="HiWi Positions"/>
            </a>
          </div>
          <div class="position-item">
            <a href="https://timexaigroup.github.io/TimeXAI-Hugo-Page/thesis-offers">
              <img src="https://timexaigroup.github.io/TimeXAI-Hugo-Page/uploads/thesis_icon.png" alt="Thesis Opportunities"/>
            </a>
          </div>
        </div>
      </div>
  design:
    columns: '1'
    spacing:
      padding: ['60px','30px','60px','30px']
---
