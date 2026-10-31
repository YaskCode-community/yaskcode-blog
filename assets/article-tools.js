(() => {
  "use strict";
  const root = "/yaskcode-blog/";
  const articles = [
    {slug:"historia-campus-yaskcode",title:"Campus YaskCode: la historia de un espacio digital para aprender",section:"Comunidad YaskCode"},
    {slug:"por-que-aprender-poo-en-la-era-de-la-ia",title:"Si la IA genera código, ¿por qué aprender POO?",section:"Ingeniería de Software"},
    {slug:"rag-fundamentos-arquitectura",title:"RAG: fundamentos y arquitectura para comenzar",section:"Inteligencia Artificial"},
    {slug:"hugging-face-modelos-datasets-ciencia-de-datos",title:"Hugging Face: modelos, datasets y herramientas para comenzar",section:"Ciencia de Datos"}
  ];
  const links = {
    "historia-campus-yaskcode":["por-que-aprender-poo-en-la-era-de-la-ia","rag-fundamentos-arquitectura"],
    "por-que-aprender-poo-en-la-era-de-la-ia":["rag-fundamentos-arquitectura","hugging-face-modelos-datasets-ciencia-de-datos"],
    "rag-fundamentos-arquitectura":["hugging-face-modelos-datasets-ciencia-de-datos","por-que-aprender-poo-en-la-era-de-la-ia"],
    "hugging-face-modelos-datasets-ciencia-de-datos":["rag-fundamentos-arquitectura","por-que-aprender-poo-en-la-era-de-la-ia"]
  };
  const urlFor = slug => new URL(root + "posts/" + slug + "/", location.origin).href;
  const create = (tag, className, content) => {
    const el = document.createElement(tag);
    if (className) el.className = className;
    if (content !== undefined) el.textContent = content;
    return el;
  };
  const link = (label, href) => {
    const a = create("a","yc-share-action",label);
    a.href = href; a.target="_blank"; a.rel="noopener noreferrer";
    return a;
  };
  const share = (articleUrl, title, compact=false) => {
    const group = create("section","yc-share-tools"+(compact?" yc-share-tools-compact":""));
    group.setAttribute("aria-label","Compartir artículo");
    group.append(create("p","yc-share-heading","Comparte este artículo"));
    const actions = create("div","yc-share-actions");
    const copy = create("button","yc-share-action","Copiar enlace");
    copy.type="button";
    const feedback = create("span","yc-share-feedback");
    feedback.setAttribute("role","status");
    feedback.setAttribute("aria-live","polite");
    copy.addEventListener("click", async () => {
      try {
        await navigator.clipboard.writeText(articleUrl);
        feedback.textContent="Enlace copiado";
      } catch {
        feedback.textContent="No se pudo copiar. Selecciona la dirección de la página en tu navegador.";
      }
    });
    actions.append(copy);
    const native = create("button","yc-share-action","Compartir");
    native.type="button";
    native.title="Abre las aplicaciones de compartir disponibles en tu dispositivo";
    native.addEventListener("click",()=>{
      if (typeof navigator.share === "function") {
        navigator.share({title,text:title,url:articleUrl}).catch(()=>{});
      } else {
        feedback.textContent="Utiliza Copiar enlace para compartir la página.";
      }
    });
    if (typeof navigator.share === "function") actions.append(native);
    // Prioridad editorial: profesionales (LinkedIn), comunidad técnica (DEV)
    // y difusión directa en español (WhatsApp).
    actions.append(
      link("LinkedIn","https://www.linkedin.com/sharing/share-offsite/?url="+encodeURIComponent(articleUrl))
    );
    const dev = link("DEV","https://dev.to/");
    dev.classList.add("yc-share-editorial");
    dev.title = "Explorar DEV Community. Perfil oficial de YaskCode todavía pendiente de vincular.";
    dev.setAttribute("aria-label","DEV Community: explorar la comunidad de desarrolladores");
    actions.append(dev,
      link("WhatsApp","https://wa.me/?text="+encodeURIComponent(title+" "+articleUrl))
    );

    const moreToggle = create("button","yc-share-action","Más redes ▾");
    moreToggle.type = "button";
    moreToggle.title = "Mostrar canales adicionales, ordenados por afinidad con YaskCode";
    const moreList = create("div","yc-share-more-list");
    moreList.id = "yc-share-extra-" + (compact ? "top" : "bottom");
    moreList.hidden = true;
    moreList.setAttribute("role","group");
    moreList.setAttribute("aria-label","Canales adicionales para compartir");
    moreToggle.setAttribute("aria-controls",moreList.id);
    moreToggle.setAttribute("aria-expanded","false");

    const technical = create("div","yc-share-more-group");
    technical.append(create("p","yc-share-more-label","Comunidades y redes técnicas"));
    const technicalLinks = create("div","yc-share-more-options");
    technicalLinks.append(
      link("Bluesky","https://bsky.app/intent/compose?text="+encodeURIComponent(title+" "+articleUrl)),
      link("Reddit","https://www.reddit.com/submit?url="+encodeURIComponent(articleUrl)+"&title="+encodeURIComponent(title)),
      link("Mastodon","https://share.joinmastodon.org/?text="+encodeURIComponent(title+" "+articleUrl)),
      link("X","https://twitter.com/intent/tweet?text="+encodeURIComponent(title)+"&url="+encodeURIComponent(articleUrl))
    );
    technical.append(technicalLinks);

    const general = create("div","yc-share-more-group");
    general.append(create("p","yc-share-more-label","Difusión y mensajería"));
    const generalLinks = create("div","yc-share-more-options");
    generalLinks.append(
      link("Telegram","https://t.me/share/url?url="+encodeURIComponent(articleUrl)+"&text="+encodeURIComponent(title)),
      link("Threads","https://www.threads.com/intent/post?text="+encodeURIComponent(title+" "+articleUrl)),
      link("Facebook","https://www.facebook.com/sharer/sharer.php?u="+encodeURIComponent(articleUrl)),
      link("Correo","mailto:?subject="+encodeURIComponent(title)+"&body="+encodeURIComponent(title+" "+articleUrl))
    );
    general.append(generalLinks);
    moreList.append(technical,general);
    moreToggle.addEventListener("click",() => {
      const willOpen = moreList.hidden;
      moreList.hidden = !willOpen;
      moreToggle.setAttribute("aria-expanded",String(willOpen));
      moreToggle.textContent = willOpen ? "Menos redes ▴" : "Más redes ▾";
      moreToggle.title = willOpen ? "Ocultar opciones adicionales" : "Mostrar más opciones para compartir";
    });
    actions.append(moreToggle);
    group.append(actions,moreList);
    if (!compact) {
      group.append(create("p","yc-share-note",
        "DEV abre la comunidad de desarrolladores, no comparte automáticamente este artículo. La futura republicación oficial se gestionará desde YaskCode."));
    }
    group.append(feedback);
    return group;
  };
  // Contadores estáticos, sin llamadas a Workers ni exposición de credenciales.
  // Solo mostramos datos verificados y recientes; nunca inventamos cifras.
  const initViews = async () => {
    try {
      const source = new URL(root + "assets/views.json", location.origin);
      const response = await fetch(source.href, {cache:"no-store"});
      if (!response.ok) return;
      const stats = await response.json();
      const ageMs = Date.now() - Date.parse(stats.generated_at);
      if (stats.schema_version !== 2 || stats.window_days !== 30 ||
          !Number.isFinite(ageMs) || ageMs < -600000 || ageMs > 72*3600*1000 ||
          !stats.paths || typeof stats.paths !== "object") return;

      const valid = counts => counts && Number.isSafeInteger(counts.total) &&
        Number.isSafeInteger(counts.last_30_days) && counts.total >= 0 &&
        counts.last_30_days >= 0 && counts.last_30_days <= counts.total;
      const badge = counts => {
        const plural = counts.total === 1 ? "vista acumulada" : "vistas acumuladas";
        const el = create("p","yc-view-count","◉ " + counts.total.toLocaleString("es") +
          " " + plural + " · " + counts.last_30_days.toLocaleString("es") +
          " últimos 30 días");
        el.title = "Desde el 31 de octubre de 2026. Vistas registradas, no visitantes únicos. La medición puede omitir navegadores con bloqueo de analítica.";
        return el;
      };
      const article = location.pathname.match(/\/posts\/([^/]+)\/?(?:index\.html)?$/);
      if (article) {
        const path = root + "posts/" + article[1] + "/";
        const number = stats.paths[path];
        const header = document.querySelector("#title-block-header");
        if (header && valid(number)) header.append(badge(number));
      }
      document.querySelectorAll("#article-grid .post-card").forEach(card => {
        const link = card.querySelector("h2 a");
        const body = card.querySelector(".card-body");
        if (!link || !body) return;
        let path = new URL(link.href,location.href).pathname;
        if (path.endsWith("/index.html")) path = path.slice(0,-10);
        if (!path.endsWith("/")) path += "/";
        const number = stats.paths[path];
        if (valid(number)) body.append(badge(number));
      });
    } catch {
      // Si no hay cifras confiables, el blog sigue funcionando sin mostrarlas.
    }
  };
  // Un solo gesto positivo por artículo, alojado por Pagemoji.
  // No usa Cloudflare Workers ni modifica las reacciones de los comentarios en GitHub.
  const positiveLike = slug => {
    const section = create("section", "yc-like-tools");
    section.setAttribute("aria-label", "Me gusta este artículo");
    const widget = document.createElement("pagemoji-reactions");
    widget.setAttribute("emojis", "💜");
    widget.setAttribute("label", "Me gusta");
    widget.setAttribute("variant", "outline");
    widget.setAttribute("page", "yaskcode-blog-" + slug);
    section.append(widget);
    return section;
  };
  const loadPositiveLikes = () => {
    if (document.querySelector("script[data-yc-pagemoji]")) return;
    const script = document.createElement("script");
    script.src = "https://pagemoji.magicpages.co/v1/pagemoji.js";
    script.defer = true;
    script.setAttribute("data-yc-pagemoji", "");
    document.head.append(script);
  };
  const init = () => {
    void initViews();
    const match = location.pathname.match(/\/posts\/([^/]+)\/?(?:index\.html)?$/);
    if (!match) return;
    const slug=match[1];
    if (!articles.some(x=>x.slug===slug)) return;
    const content = document.querySelector("#quarto-document-content") || document.querySelector("main.content");
    if (!content) return;
    const canonical = urlFor(slug);
    const title=document.querySelector("h1.title")?.textContent?.trim() || document.title;
    const top=share(canonical,title,true);
    const subtitle = content.querySelector("p");
    const like = positiveLike(slug);
    if (subtitle) {
      subtitle.insertAdjacentElement("beforebegin",top);
      top.insertAdjacentElement("beforebegin",like);
    } else {
      content.prepend(top);
      content.prepend(like);
    }
    loadPositiveLikes();
    content.append(share(canonical,title));
    const related=create("nav","yc-related");
    related.setAttribute("aria-label","Lecturas relacionadas");
    related.append(create("h2","","Continúa explorando"));
    const items=create("ul","yc-related-list");
    for(const id of links[slug]||[]){
      const info=articles.find(x=>x.slug===id);
      if(!info) continue;
      const li=create("li","");
      const a=create("a","",info.title);a.href=urlFor(info.slug);
      li.append(a,create("small","",info.section));
      items.append(li);
    }
    related.append(items);
    content.append(related);
  };
  if(document.readyState==="loading") document.addEventListener("DOMContentLoaded",init);
  else init();
})();
