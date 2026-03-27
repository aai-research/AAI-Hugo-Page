---
title: ""
#Paper-Page
type: page
_build:
  list: false
---

<section class="publications-page">
  <header class="publications-header">
    <h1>{{ .Title }}</h1>
    <p>A collection of research papers and publications from the TimeXAI group. Click on the title to view the full paper.</p>
  </header>

  <section class="publications-list">
    {{ partial "publications.html" . }}
  </section>
</section>
