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
          <h1 class="text-center">Applied AI-Lab</h1>
          <p class="text-center">
            We are exploring practical and innovative solutions in projects in the field of artificial intelligence and contribute to the advancement of knowledge. At the same time, we are committed to teaching and mentoring the next generation of AI engineers. By combining theory and practice, we are working to make AI more accessible, responsible, and effective.
          </p>
        </div>
        <div class="home-about-icons">
          <div class="care-item">
            <a href="{{ "/appliedAI/" | relURL }}" class="care-inner">
              <img src="{{ "/uploads/aai_icon2.png" | relURL }}" alt="Applied AI"/>
            </a>
          </div>
          <div class="care-item">
            <a href="{{ "/research" | relURL }}" class="care-inner">
              <img src="{{ "/uploads/project_icon2.png" | relURL }}" alt="Projects"/>
            </a>
          </div>
          <div class="care-item">
            <a href="{{ "/students" | relURL }}" class="care-inner">
              <img src="{{ "/uploads/teaching_icon2.png" | relURL }}" alt="Students"/>
            </a>
          </div>
          <div class="care-item">
            <a href="{{ "/publications" | relURL }}" class="care-inner">
              <img src="{{ "/uploads/paper_icon2.png" | relURL }}" alt="Publications"/>
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
        <a href="{{ "/appliedAI/" | relURL }}" target="_blank">
          <img src="{{ "/uploads/aai_logo.png" | relURL }}" alt="Applied AI Lab"/>
        </a>
        <a href="https://www.thm.de/kompetenzzentren/kite/profil.html" target="_blank">
         <img src="{{ "/uploads/kite_logo.png" | relURL }}" alt="KITE"/>
        </a>
        <a href="https://www.thm.de" target="_blank">
          <img src="{{ "/uploads/THM_logo.png" | relURL }}" alt="THM"/>
        </a>
        <a href="https://hessian.ai" target="_blank">
          <img src="{{ "/uploads/HessenAi_logo.png" | relURL }}" alt="HessenAI"/>
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
              <img src="{{ "/uploads/thm_job_icon.png" | relURL }}" alt="THM Jobs"/>
            </a>         
          </div>
          <div class="position-item">
            <a href="/hiwi-offers">
              <img src="{{ "/uploads/hiwi_job_icon.png" | relURL }}" alt="HiWi Positions"/>
            </a>
          </div>
          <div class="position-item">
            <a href="/thesis-offers">
              <img src="{{ "/uploads/thesis_icon.png" | relURL }}" alt="Thesis Opportunities"/>
            </a>
          </div>
        </div>
      </div>
  design:
    columns: '1'
    spacing:
      padding: ['60px','30px','60px','30px']
---
