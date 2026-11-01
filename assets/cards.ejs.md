<%
const sequence = {
  "ruta-aprendizaje-yaskcode-rag-sistemas-multiagentes": 1,
  "leer-criticamente-caso-ia-evidencia-arquitectura-limites": 2,
  "runcoach-ai-conocimiento-rag-caso": 3,
  "runcoach-rag-consultas-contextuales-practica": 4,
  "evaluar-recuperacion-rag-precision-recall-mrr": 5,
  "seniorvital-rag-agentes-evidencia-caso": 6,
  "seniorvital-evidencia-abstencion-rag-practica": 7,
  "de-rag-a-sistemas-multiagentes-responsabilidades-supervision": 8
};
const slugFromPath = path => String(path || "").match(/posts\/([^/]+)\//)?.[1] || "";
// Quarto ordena por fecha descendente. En la fecha de publicación compartida,
// preservamos la secuencia pedagógica aprobada, sin inventar fechas distintas.
const orderedItems = items.slice().sort((a, b) => {
  const left = sequence[slugFromPath(a.path)];
  const right = sequence[slugFromPath(b.path)];
  return left && right ? left - right : 0;
});
%>
```{=html}
<div class="article-grid" id="article-grid">
<% for (const item of orderedItems) { const order = sequence[slugFromPath(item.path)]; %>
  <article class="post-card" data-area="<%- item.area || '' %>" data-section="<%- item['editorial-section'] || '' %>">
    <% if (item.image) { %>
    <a class="card-image-link" href="<%- item.path %>" tabindex="-1" aria-hidden="true"><img src="<%- item.image %>" alt="" width="1200" height="630" loading="lazy"></a>
    <% } %>
    <div class="card-body">
      <div class="card-tags"><% if (item['editorial-section']) { %><span><%- item['editorial-section'] %></span><% } %><% if (item.area) { %><span><%- item.area %></span><% } %><% if (item.level) { %><span><%- item.level %></span><% } %></div>
      <p class="card-date">Publicado: <%- item.date %><% if (order) { %><span class="card-series-order">Serie YaskCode · Entrega <%- order %> de 8</span><% } %></p>
      <h2><a href="<%- item.path %>"><%- item.title %></a></h2>
      <p class="card-description"><%- item.description || '' %></p>
      <p class="card-author"><%- Array.isArray(item.author) ? item.author.join(', ') : (item.author || 'YaskCode') %></p>
    </div>
  </article>
<% } %>
</div>

```
