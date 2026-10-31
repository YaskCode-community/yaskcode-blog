```{=html}
<div class="article-grid" id="article-grid">
<% for (const item of items) { %>
  <article class="post-card" data-area="<%- item.area || '' %>" data-section="<%- item['editorial-section'] || '' %>">
    <% if (item.image) { %>
    <a class="card-image-link" href="<%- item.path %>" tabindex="-1" aria-hidden="true"><img src="<%- item.image %>" alt="" width="1200" height="630" loading="lazy"></a>
    <% } %>
    <div class="card-body">
      <div class="card-tags"><% if (item['editorial-section']) { %><span><%- item['editorial-section'] %></span><% } %><% if (item.area) { %><span><%- item.area %></span><% } %><% if (item.level) { %><span><%- item.level %></span><% } %></div>
      <p class="card-date"><%- item.date %></p>
      <h2><a href="<%- item.path %>"><%- item.title %></a></h2>
      <p class="card-description"><%- item.description || '' %></p>
      <p class="card-author"><%- Array.isArray(item.author) ? item.author.join(', ') : (item.author || 'YaskCode') %></p>
    </div>
  </article>
<% } %>
</div>
```
