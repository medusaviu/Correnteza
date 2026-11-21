from pathlib import Path
base = Path("/mnt/data")
html = """<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#050505">
  <meta name="description" content="Correnteza — Outras formas de representar o Sertão. Long-form jornalístico de Cibelle Vieira.">
  <title>Correnteza — Outras formas de representar o Sertão</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header class="site-header">
    <a class="brand-mark" href="#inicio" aria-label="Correnteza — início">
      <img src="assets/images/logo-correnteza.png" alt="">
    </a>

    <button class="menu-toggle" type="button" aria-label="Abrir menu"
      aria-expanded="false" aria-controls="main-navigation">
      <span></span><span></span><span></span>
    </button>

    <nav class="main-navigation" id="main-navigation" aria-label="Navegação principal">
      <a href="#inicio">Início</a>
      <a href="#a-margem-do-palco">À Margem do Palco</a>
      <a href="#linha-do-tempo">Linha do Tempo</a>
      <a href="#nucleo-biruta">Núcleo Biruta</a>
      <a href="#coletivo-abdias">Coletivo Abdias</a>
      <a href="#caatingayro">Caatingayro</a>
      <a href="#artistas">Artistas</a>
      <a href="#lugares">Lugares</a>
    </nav>
  </header>

  <main>
    <section class="home" id="inicio">
      <div class="cover">
        <img class="cover-art" src="assets/images/elemento-azul-capa.png" alt="">
        <div class="cover-content">
          <h1>Correnteza</h1>
          <p class="cover-subtitle">Outras formas de representar o Sertão</p>
          <p class="cover-author">por Cibelle Vieira</p>
        </div>
      </div>

      <article class="opening">
        <div class="opening-heading">
          <h2>Entre duas margens, uma<br class="desktop-break"> só correnteza</h2>
          <figure class="character">
            <img src="assets/images/ilustracao-personagem.png" alt="Ilustração de uma personagem">
            <figcaption>Descrição da imagem</figcaption>
          </figure>
        </div>

        <div class="article-copy">
          <p>A escrita deste texto nasce de um incômodo e, desse incômodo, surge uma pergunta: como documentar existências que foram negadas, silenciadas ou deixadas à margem das narrativas sobre o lugar onde vivem?</p>

          <p>Nasci em Juazeiro, na Bahia, e vivi a vida inteira em Petrolina, Pernambuco. Certa vez, durante uma apresentação de trabalho em Salvador, mencionei esse fato. A reação foi de desconfiança: perguntaram se aquilo era uma piada. Respondi com outra pergunta: por que seria?</p>

          <p>Mas minha história entre essas duas margens não tem nada de extraordinário para quem cresceu por aqui. Meu nascimento, assim como o de tantas outras pessoas da minha geração, também atravessa um período de dificuldades na saúde pública de Petrolina, quando nascer em uma cidade e buscar atendimento na outra se tornou parte da realidade de muitas famílias.</p>

          <p>É assim que se vive entre Petrolina e Juazeiro: cidades separadas por uma divisa estadual, mas aproximadas pelo Rio Opará, o São Francisco, e por uma vida cotidiana que não cabe nas fronteiras dos mapas. Quando falta de um lado, atravessa-se para o outro. Trabalha-se em uma cidade, estuda-se na outra, constroem-se afetos, histórias e pertencimentos que circulam entre as duas margens. Somos pernambaianos, PEBA's, como gostamos de dizer. E não há contradição nisso.</p>
        </div>

        <div class="photo-gallery" aria-label="Fotografias da reportagem">
          <figure><img src="assets/images/fotografia-1.jpg" alt="Registro fotográfico da reportagem"></figure>
          <figure><img src="assets/images/fotografia-2.jpg" alt="Registro fotográfico da reportagem"></figure>
          <figure><img src="assets/images/fotografia-3.jpg" alt="Registro fotográfico da reportagem"></figure>
        </div>

        <div class="article-copy article-continuation">
          <p>Por isso, ao conversar com artistas, educadores e agentes culturais para construir esta reportagem, entendi que não seria possível contar essas experiências olhando apenas para uma das cidades. A arte produzida neste território também atravessa pontes, margens e fronteiras. Ela acontece em rede, em encontros, em movimentos de troca, como uma correnteza. Corre como o rio que costura essas duas cidades e alimenta tantas formas de existir no Semiárido.</p>

          <p>Mas nenhuma história começa exatamente onde a gente decide contá-la. Para compreender as expressões artísticas que existem hoje, é preciso reconhecer os caminhos que vieram antes, as memórias que permanecem e as histórias que nem sempre encontraram espaço para serem narradas.</p>
        </div>
      </article>
    </section>

    <!-- As seções abaixo são âncoras de navegação. O conteúdo será inserido
         quando as páginas correspondentes do projeto Canva estiverem prontas. -->
    <section class="reserved-section" id="a-margem-do-palco" aria-label="À Margem do Palco"></section>
    <section class="reserved-section" id="linha-do-tempo" aria-label="Linha do Tempo"></section>
    <section class="reserved-section" id="nucleo-biruta" aria-label="Núcleo Biruta"></section>
    <section class="reserved-section" id="coletivo-abdias" aria-label="Coletivo Abdias"></section>
    <section class="reserved-section" id="caatingayro" aria-label="Caatingayro"></section>
    <section class="reserved-section" id="artistas" aria-label="Artistas"></section>
    <section class="reserved-section" id="lugares" aria-label="Lugares"></section>
  </main>

  <footer class="site-footer">
    <p>Correnteza — Outras formas de representar o Sertão</p>
    <p>Long-form jornalístico | Trabalho de Conclusão de Curso — Graduação em Jornalismo, Universidade do Estado da Bahia (UNEB)</p>
    <p>Autoria: Cibelle Vieira | Orientação: Raiane Sousa | Design e desenvolvimento do site: Jenifer Silva © 2026</p>
  </footer>

  <script src="script.js"></script>
</body>
</html>
"""
css = """@charset "UTF-8";

/* Correnteza — estilos da página inicial */
:root {
  --black: #050505;
  --white: #f5f4f1;
  --nav-bg: #f7f7f5;
  --nav-text: #292929;
  --muted: #a9a9a9;
  --blue: #343c91;
  --header-height: 48px;
}

* { box-sizing: border-box; }
html { scroll-behavior: smooth; background: var(--black); }
body {
  margin: 0;
  background: var(--black);
  color: var(--white);
  font-family: "Neue Montreal", "Arial", sans-serif;
}
img { display: block; max-width: 100%; }
a { color: inherit; text-decoration: none; }

.site-header {
  position: sticky;
  z-index: 50;
  top: 0;
  min-height: var(--header-height);
  padding: 0 18px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  background: var(--nav-bg);
  color: var(--nav-text);
}
.brand-mark {
  width: 30px;
  height: 30px;
  flex: 0 0 30px;
  overflow: hidden;
}
.brand-mark img { width: 100%; height: 100%; object-fit: contain; }

.main-navigation {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: clamp(12px, 1.65vw, 25px);
  white-space: nowrap;
  font-size: clamp(11px, 1.05vw, 14px);
}
.main-navigation a { transition: opacity .2s ease; }
.main-navigation a:hover,
.main-navigation a:focus-visible { opacity: .55; }

.menu-toggle {
  display: none;
  width: 38px;
  height: 36px;
  padding: 8px;
  border: 0;
  background: transparent;
  cursor: pointer;
}
.menu-toggle span {
  display: block;
  height: 2px;
  margin: 4px 0;
  background: var(--nav-text);
}

.home { background: var(--black); }
.cover {
  position: relative;
  min-height: clamp(230px, 28vw, 390px);
  display: grid;
  place-items: center;
  overflow: hidden;
  isolation: isolate;
  background: #050505;
}
.cover-art {
  position: absolute;
  z-index: -1;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
}
.cover-content {
  width: min(94%, 1200px);
  padding: 46px 0;
  text-align: center;
}
.cover h1 {
  margin: 0;
  color: #fff;
  font-family: "Cubao Free Wide", Impact, sans-serif;
  font-size: clamp(3.3rem, 10.8vw, 9rem);
  font-weight: 900;
  line-height: .82;
  letter-spacing: .015em;
  text-transform: uppercase;
}
.cover-subtitle {
  margin: 12px 0 0;
  font-family: "Glacial Indifference", Arial, sans-serif;
  font-size: clamp(.65rem, 1.25vw, .95rem);
  letter-spacing: .1em;
  text-transform: uppercase;
}
.cover-author {
  margin: 8px 0 0;
  color: #d0d0d0;
  font-size: 10px;
  letter-spacing: .12em;
  text-transform: uppercase;
}

.opening {
  width: min(100%, 1440px);
  margin: 0 auto;
  padding: 30px clamp(22px, 4.2vw, 64px) 64px;
}
.opening-heading {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(110px, 190px);
  align-items: center;
  gap: 24px;
  margin-bottom: 18px;
}
.opening-heading h2 {
  max-width: 850px;
  margin: 0;
  font-family: "Glacial Indifference", Arial, sans-serif;
  font-size: clamp(1.65rem, 4vw, 3.35rem);
  font-weight: 400;
  line-height: 1.08;
  letter-spacing: .025em;
  text-transform: uppercase;
}
.character { width: 100%; margin: 0; }
.character img { width: 100%; height: auto; object-fit: contain; }
.character figcaption {
  margin-top: 5px;
  color: var(--muted);
  font-size: 9px;
  text-align: center;
}
.article-copy {
  max-width: 1160px;
  font-family: "Glacial Indifference", Arial, sans-serif;
  font-size: clamp(.88rem, 1.15vw, 1.03rem);
  line-height: 1.55;
}
.article-copy p { margin: 0 0 17px; }

.photo-gallery {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 10px;
  margin: 28px 0 25px;
}
.photo-gallery figure {
  min-width: 0;
  aspect-ratio: 1.42;
  margin: 0;
  overflow: hidden;
  background: #151515;
}
.photo-gallery img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform .45s ease;
}
.photo-gallery figure:hover img { transform: scale(1.025); }
.article-continuation p:last-child { margin-bottom: 0; }

.reserved-section {
  min-height: 65vh;
  scroll-margin-top: var(--header-height);
  background: var(--black);
}

.site-footer {
  padding: 30px 22px 34px;
  border-top: 1px solid #252525;
  color: #bdbdbd;
  font-family: "Glacial Indifference", Arial, sans-serif;
  font-size: 12px;
  line-height: 1.55;
  text-align: center;
}
.site-footer p { margin: 4px 0; }
.site-footer p:first-child {
  color: #fff;
  font-size: 15px;
  font-weight: 600;
}

@media (max-width: 900px) {
  .site-header { padding: 0 14px; }
  .main-navigation { gap: 11px; font-size: 11px; }
}
@media (max-width: 720px) {
  :root { --header-height: 54px; }
  .site-header { padding: 0 15px; }
  .menu-toggle { display: block; margin-left: auto; }
  .main-navigation {
    position: absolute;
    top: var(--header-height);
    right: 0;
    left: 0;
    display: none;
    align-items: flex-start;
    flex-direction: column;
    gap: 0;
    padding: 8px 20px 16px;
    background: var(--nav-bg);
    box-shadow: 0 8px 16px rgb(0 0 0 / 18%);
    white-space: normal;
    font-size: 14px;
  }
  .main-navigation.is-open { display: flex; }
  .main-navigation a { width: 100%; padding: 10px 0; }
  .cover { min-height: 250px; }
  .opening { padding-top: 30px; }
  .opening-heading {
    grid-template-columns: minmax(0, 1fr) 105px;
    gap: 10px;
  }
  .opening-heading h2 { font-size: clamp(1.45rem, 6vw, 2.3rem); }
  .photo-gallery { grid-template-columns: 1fr; gap: 10px; }
  .photo-gallery figure { aspect-ratio: 1.55; }
  .site-footer { padding: 26px 18px; }
}
@media (max-width: 420px) {
  .opening-heading { grid-template-columns: minmax(0, 1fr) 86px; }
  .article-copy { line-height: 1.5; }
  .cover { min-height: 215px; }
  .desktop-break { display: none; }
}
"""
js = """const menuButton = document.querySelector(".menu-toggle");
const navigation = document.querySelector(".main-navigation");

if (menuButton && navigation) {
  menuButton.addEventListener("click", () => {
    const isOpen = navigation.classList.toggle("is-open");
    menuButton.setAttribute("aria-expanded", String(isOpen));
    menuButton.setAttribute("aria-label", isOpen ? "Fechar menu" : "Abrir menu");
  });

  navigation.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      navigation.classList.remove("is-open");
      menuButton.setAttribute("aria-expanded", "false");
      menuButton.setAttribute("aria-label", "Abrir menu");
    });
  });
}
"""
(base/"index.html").write_text(html, encoding="utf-8")
(base/"styles.css").write_text(css, encoding="utf-8")
(base/"script.js").write_text(js, encoding="utf-8")
print("Arquivos criados:", *(str(base/n) for n in ["index.html","styles.css","script.js"]), sep="\n")
