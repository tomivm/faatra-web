const mockNewItem = {
  id: 1,
  title: "REUNIÓN FORMATIVA - 10 oct. 2021",
  description:
    "Los boletines de prensa ofrecen una forma increíble de informar a los clientes sobre nuestros nuevos productos y servicios, eventos, premios y mucho más.",
  imageSrc: "./../images/quienes-somos/quienes-somos-full-side.png",
  url: "./../trainings/capacitacion-full.html",
};

const mockNewsList = Array(15)
  .fill()
  .map(() => mockNewItem);

const PAGE_MAX_ITEMS = 4;

function getPages(mockNewsList) {
  return Math.ceil(mockNewsList.length / PAGE_MAX_ITEMS);
}
const getNewsActualPage = (actualPage, newsList) => {
  return newsList.slice(
    (actualPage - 1) * PAGE_MAX_ITEMS,
    actualPage * PAGE_MAX_ITEMS
  );
};

const newsPageState = {
  actualPage: 1,
  totalPages: getPages(mockNewsList),
};

function changePage({ actualPage, totalPages }) {
  const newsActualPage = getNewsActualPage(actualPage, mockNewsList);

  const renderActualPage = (newsActualPage) => {
    const createNewItem = ({ title, description, imageSrc, url }) => {
      const newItem = document.createElement("a");
      newItem.classList.add("new-item");

      const createSideImage = () => {
        const image = document.createElement("img");
        image.src = imageSrc;
        return image;
      };

      const createTextContainer = () => {
        const textContainer = document.createElement("div");
        textContainer.classList.add("new-text-container");

        const h1 = document.createElement("h1");
        const titleTextNode = document.createTextNode(title);
        h1.appendChild(titleTextNode);

        const p = document.createElement("p");
        const descriptionTextNode = document.createTextNode(description);
        p.appendChild(descriptionTextNode);

        textContainer.appendChild(h1);
        textContainer.appendChild(p);
        return textContainer;
      };
      newItem.appendChild(createSideImage());
      newItem.appendChild(createTextContainer());
      newItem.href = url;
      return newItem;
    };

    const newsItemsContainer = document.getElementById("news-items-container");

    newsItemsContainer.innerHTML = "";

    newsActualPage.map((trainingItem) => {
      const item = createNewItem(trainingItem);

      newsItemsContainer.appendChild(item);
    });
  };
  const renderPagesNavigator = ({ actualPage, totalPages }) => {
    const pagesNavigator = document.getElementById("pages-nav-id");

    const createPageNavButton = (number) => {
      const navButton = document.createElement("div");
      const symbol = document.createTextNode(number);
      const handlePageClick = () => {
        changePage({ actualPage: number, totalPages });
        window.scroll({
          top: 0,
          left: 0,
          behavior: "smooth",
        });
      };
      navButton.appendChild(symbol);
      navButton.classList.add("page-btn");
      navButton.classList.add("scale-hover");
      navButton.onclick = handlePageClick;
      if (number === actualPage) navButton.classList.add("page-selected");
      return navButton;
    };

    pagesNavigator.innerHTML = "";

    for (let i = 1; i <= totalPages; i++) {
      const navButton = createPageNavButton(i);
      pagesNavigator.appendChild(navButton);
    }
  };

  renderActualPage(newsActualPage);
  renderPagesNavigator({ actualPage, totalPages });
}

window.onload = init;

function init() {
  changePage(newsPageState);
}
