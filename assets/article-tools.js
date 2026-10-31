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
    native.addEventListener("click",()=>{
      if (typeof navigator.share === "function") {
        navigator.share({title,text:title,url:articleUrl}).catch(()=>{});
      } else {
        feedback.textContent="Utiliza Copiar enlace para compartir la página.";
      }
    });
    if (typeof navigator.share === "function") actions.append(native);
    // Las dos acciones principales permanecen visibles; el resto se agrupa para móviles.
    actions.append(
      link("WhatsApp","https://wa.me/?text="+encodeURIComponent(title+" "+articleUrl)),
      link("LinkedIn","https://www.linkedin.com/sharing/share-offsite/?url="+encodeURIComponent(articleUrl))
    );
    const more = create("details","yc-share-more");
    const summary = create("summary","yc-share-action","Más redes");
    const moreList = create("div","yc-share-more-list");
    moreList.append(
      link("Bluesky","https://bsky.app/intent/compose?text="+encodeURIComponent(title+" "+articleUrl)),
      link("Telegram","https://t.me/share/url?url="+encodeURIComponent(articleUrl)+"&text="+encodeURIComponent(title)),
      link("X","https://twitter.com/intent/tweet?text="+encodeURIComponent(title)+"&url="+encodeURIComponent(articleUrl)),
      link("Facebook","https://www.facebook.com/sharer/sharer.php?u="+encodeURIComponent(articleUrl)),
      link("Threads","https://www.threads.com/intent/post?text="+encodeURIComponent(title+" "+articleUrl)),
      link("Mastodon","https://share.joinmastodon.org/?text="+encodeURIComponent(title+" "+articleUrl)),
      link("Reddit","https://www.reddit.com/submit?url="+encodeURIComponent(articleUrl)+"&title="+encodeURIComponent(title)),
      link("Correo","mailto:?subject="+encodeURIComponent(title)+"&body="+encodeURIComponent(title+"\n"+articleUrl))
    );
    const instagram = create("button","yc-share-action","Instagram · copiar enlace");
    instagram.type="button";
    instagram.addEventListener("click", async () => {
      try {
        await navigator.clipboard.writeText(articleUrl);
        feedback.textContent="Enlace copiado. Puedes pegarlo en Instagram, por ejemplo en Stories mediante el sticker de enlace.";
      } catch {
        feedback.textContent="Para Instagram, copia la dirección de esta página desde tu navegador.";
      }
    });
    moreList.append(instagram);
    more.append(summary,moreList);
    actions.append(more);
    group.append(actions,feedback);
    return group;
  };
  const init = () => {
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
    if(subtitle) subtitle.insertAdjacentElement("beforebegin",top);
    else content.prepend(top);
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
