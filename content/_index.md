---
# Home-Page
title: Home
type: landing

sections:

# ======================
# TITEL IMAGE SMALLER WIDTH
# ======================
#- block: markdown
#  content:
#    text: |
#      <div class="hero-home-small">
#          <img src="https://timexaigroup.github.io/TimeXAI-Hugo-Page/uploads/teaser_homepage_aaiLab_small.png" alt="Hero Image"/>
#      </div>
#  design:
#    columns: '1'
#    spacing:
#      padding: ['0','0','0','0']
#    css_class: hero-centered
  
# ======================
# TITEL IMAGE FULL WIDTH
# ======================
- block: markdown
  content:
    text: |
      <div class="hero-home">
          <img src="uploads/teaser_homepage_aaiLab_small.png" alt="Applied AI Lab at Technische Hochschule Mittelhessen"/>
      </div>
  design:
    columns: '1'
    spacing:
      padding: ['0','0','0','0']
    css_class: hero-fullwidth

# ======================
# SHORT RESEARCH PROFILE + GROUP PHOTO
# ======================
- block: markdown
  content:
    text: |
      <section class="home-profile">
      <div class="home-profile__content">

        <h1 class="home-profile__title">Applied AI Lab</h1>

        <p class="home-profile__lead">
          We develop novel methods for trustworthy and explainable AI for time series, images, and video. Our research combines methodological advances in reliable machine learning with challenging interdisciplinary applications in science, engineering, and healthcare.
        </p>

        <p class="home-profile__leadership">
          Led by <a href="/team/hannig/">Prof. Dr. Jennifer Hannig</a> at Technische Hochschule Mittelhessen and hessian.AI.
        </p>

       <div class="home-profile__actions">
        <a class="home-button" href="/research/">Explore our research</a>
        <a class="home-button" href="/team/">Meet the team</a>
      </div>

      </div>

      <div class="home-profile__image">
      <img
        src="/uploads/group_photo_small_2026.jpg"
        alt="Members of the Applied AI Lab at Technische Hochschule Mittelhessen"
        loading="lazy"
        decoding="async"
      />
      </div>
      </section>
  design:
    columns: '1'
    css_class: home-profile-section
    spacing:
      padding: ['50px', '20px', '50px', '20px']  

# ======================
# INTRO + ANIMATION ICONS
# ======================
#- block: markdown
#  content:
#    text: |
#      <div class="home-intro-icons text-center">
#        <div class="home-intro">        
#          <h1 class="text-center">Applied AI Lab</h1>
#          <p class="text-center">
#            We develop novel methods for trustworthy and explainable AI for time series, images, and video. Our research combines methodological advances in reliable machine learning with challenging interdisciplinary   applications in science, engineering, and healthcare.</p>
#          <p class="home-intro__leadership">
#           The Applied AI Lab is headed by <a href="/team/hannig/"> Prof. Dr. Jennifer Hannig</a>, Professor of Artificial Intelligence at Technische Hochschule Mittelhessen.</p>
#        </div>
#        <div class="home-about-icons">
#          <div class="care-item">
#            <a href="aai/" class="care-inner">
#              <img src="uploads/aai_icon2.png" alt=""/>
#              <span class="care-label">About Us</span>
#            </a>
#          </div>
#          <div class="care-item">
#            <a href="research" class="care-inner">
#               <img src="uploads/project_icon2.png" alt=""/>
#               <span class="care-label">Projects</span>
#            </a>
#          </div>
#          <div class="care-item">
#            <a href="students" class="care-inner">
#              <img src="uploads/teaching_icon2.png" alt=""/>
#              <span class="care-label">Teaching</span>
#            </a>
#          </div>
#          <div class="care-item">
#            <a href="publication" class="care-inner">
#              <img src="uploads/paper_icon2.png" alt=""/>
#              <span class="care-label">Publications</span>
#            </a>
#          </div>
#        </div>
#      </div>
#  design:
#    columns: '1'
#    spacing:
#      padding: ['80px','30px','80px','30px']

# ======================
# PARTNER LOGOS
# ======================
- block: markdown
  content:
    text: |
      <div class="hero-partner-logos text-center">
      <a href="/aai/" aria-label="Applied AI Lab">
      <img src="/uploads/aai_lab.png" alt="Applied AI Lab logo" />
      </a>
      <a href="https://www.thm.de/kompetenzzentren/kite/profil.html" target="_blank" rel="noopener noreferrer" aria-label="KITE website – opens in a new tab">
      <img src="/uploads/kite_logo.png" alt="KITE logo" />
      </a>
      <a href="https://www.thm.de" target="_blank" rel="noopener noreferrer" aria-label="Technische Hochschule Mittelhessen website – opens in a new tab">
      <img src="/uploads/THM_logo.png" alt="Technische Hochschule Mittelhessen logo" />
      </a>
      <a href="https://hessian.ai" target="_blank" rel="noopener noreferrer" aria-label="hessian.AI website – opens in a new tab">
      <img src="/uploads/HessenAi_logo.png" alt="hessian.AI logo" />
      </a>
      </div>
  design:
    columns: '1'
    css_class: home-partners-section
    spacing:
      padding: ['20px', '0', '70px', '0']

# ======================
# SELECTED PROJECTS
# ======================
- block: markdown
  content:
    text: |
      <section class="home-projects">
      <header class="home-projects__header">
      <p class="home-section-label">Current Research</p>
      <h2>Selected Projects</h2>
      </header>

      <div class="home-projects__grid">

      <article class="home-project-card">
      <div class="home-project-card__image">
      <img src="/uploads/time_series.jpg" alt="Visualization of time-series data for the TimeXAI project" loading="lazy" decoding="async" />
      </div>
      <div class="home-project-card__content">
      <h3>TimeXAI</h3>
      <p>We develop and evaluate explainable AI methods for complex time-series classification models.</p>
      <p class="home-project-card__meta">BMFTR · ExperTeam4KI · 2024–2027</p>
      <a href="/research/project_timexai/">Explore project →</a>
      </div>
      </article>

      <article class="home-project-card">
      <div class="home-project-card__image">
      <img src="/uploads/VisSURG-AID.png" alt="Illustration of visual artificial intelligence for surgical decision support" loading="lazy" decoding="async" />
      </div>
      <div class="home-project-card__content">
      <h3>VisSURG-AID</h3>
      <p>We investigate transparent visual AI methods for reliable decision support based on surgical video.</p>
      <p class="home-project-card__meta">FCMH Experimentierräume · 2026</p>
      <a href="/research/project_vissurg_aid/">Explore project →</a>
      </div>
      </article>

      </div>

      <div class="home-projects__all">
      <a class="home-button" href="/research/">View all research projects</a>
      </div>
      </section>
  design:
    columns: '1'
    css_class: home-projects-section
    spacing:
      padding: ['65px', '20px', '70px', '20px']

# ======================
# RECENT PUBLICATIONS
# ======================
- block: collection
  content:
    text: |
      <div class="home-publications__header">
      <p class="home-section-label">Selected Publications</p>
      <h2>Recent Research Outputs</h2>
      </div>
    filters:
      folders:
        - publication
      exclude_future: true
    count: 3
    sort_by: Date
    sort_ascending: false
    archive:
      enable: true
      text: View all publications
      link: /publication/
  design:
    view: home-publication
    columns: '3'
    css_class: home-publications-section
    spacing:
      padding: ['60px', '20px', '70px', '20px']
  
# ======================
# FEATURED VIDEO
# ======================
- block: markdown
  content:
    text: |
      <section class="featured-video">
      <div class="featured-video__text">
      <p class="featured-video__eyebrow">Video Podcast</p>
      <h2>Making AI Understandable</h2>
      <p>In this video podcast, Prof. Dr. Jennifer Hannig discusses how eXplainable AI makes model decisions more transparent and why trustworthy AI is essential in high-stakes applications.</p>
      <a class="home-button" href="https://www.youtube.com/watch?v=OqfVpfbw1-4" target="_blank" rel="noopener noreferrer">Watch the video podcast →</a>
      </div>
      <div class="featured-video__player">
      <iframe src="https://www.youtube-nocookie.com/embed/OqfVpfbw1-4" title="Making AI Understandable with Prof. Dr. Jennifer Hannig" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
      </div>
      </section>
  design:
    columns: '1'
    css_class: home-video-section
    spacing:
      padding: ['30px', '20px', '40px', '20px']



# ======================
# LATEST NEWS
# ======================
#- block: collection
#  content:
#    text: |
#      <div class="latest-news-section">
#        <h1 class="text-center">Latest News</h1>
#        <p class="text-center">
#          Check out the latest activities!
#        </p>
#      </div>
#  filters:
#    folders:
#      - news
#    order: desc
#    limit: 3
#  design:
#    view: card
#    columns: '3'
#    css_id: news
#    show_image: true
#    show_date: true
#    show_summary: true
#    spacing:
#      padding: ['60px','30px','60px','30px']

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
          Whether you are a student, researcher, or industry expert, we welcome opportunities to collaborate on projects and exchange expertise.       
          Work with us and contribute to advancing applied artificial intelligence.
        </p>

        <div class="home-open-positions">
          <div class="position-item">
            <a href="https://www.thm.de/site/hochschule/profil/job-und-karriere/aktuelle-stellenangebote.html" target="_blank">
              <img src="uploads/thm_job_icon.png" alt=""/>
              <span class="position-label">Job Openings</span>
            </a>         
          </div>
          <div class="position-item">
            <a href="students">
              <img src="uploads/hiwi_job_icon.png" alt=""/>
              <span class="position-label">Student Opportunities</span>
            </a>
          </div>
          <div class="position-item">
            <a href="students/theses/">
              <img src="uploads/thesis_icon.png" alt=""/>
              <span class="position-label">Thesis Topics</span>
            </a>
          </div>
        </div>
      </div>
  design:
    columns: '1'
    css_class: home-open-positions-section
    spacing:
      padding: ['60px','30px','60px','30px']
---
