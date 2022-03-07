const chambersArrayMock = [
  {
    id: 0,
    name: "Carassa",
    url: "./camara-full.html",
    tooltipText: "Córdoba",
    imgUrl: "./images/logos-camaras/AMUPTRA.jpg",
  },
  {
    id: 1,
    name: "fasfasa",
    url: "Asesoria",
    tooltipText: "Córdoba",
    imgUrl: "./images/logos-camaras/ATGS_logo.jpg",
  },
  {
    id: 2,
    name: "asdaddas",
    url: "Asesoria",
    tooltipText: "Córdoba",
    imgUrl: "./images/logos-camaras/atraanes.JPG",
  },
  {
    id: 3,
    name: "Carasadfassa",
    url: "Asesoria",
    tooltipText: "Córdoba",
    imgUrl: "./images/logos-camaras/img002.jpg",
  },
  {
    id: 4,
    name: "Carasadfassa",
    url: "Asesoria",
    tooltipText: "Córdoba",
    imgUrl: "./images/logos-camaras/AMA.jpg",
  },
  {
    id: 4,
    name: "Carasadfassa",
    url: "Asesoria",
    tooltipText: "Córdoba",
    imgUrl: "./images/logos-camaras/ATA.jpg",
  },
  {
    id: 4,
    name: "Carasadfassa",
    url: "Asesoria",
    tooltipText: "Córdoba",
    imgUrl: "./images/logos-camaras/Concordia.png",
  },
  {
    id: 4,
    name: "Carasadfassa",
    url: "Asesoria",
    tooltipText: "Córdoba",
    imgUrl: "./images/logos-camaras/Mendoza.jpg",
  },
  {
    id: 4,
    name: "Carasadfassa",
    url: "Asesoria",
    tooltipText: "Córdoba",
    imgUrl: "./images/logos-camaras/APTMA.png",
  },
  {
    id: 4,
    name: "Carasadfassa",
    url: "Asesoria",
    tooltipText: "Córdoba",
    imgUrl: "./images/logos-camaras/San_Juan.png",
  },
  {
    id: 4,
    name: "Carasadfassa",
    url: "Asesoria",
    tooltipText: "Córdoba",
    imgUrl: "./images/logos-camaras/logo.jpg",
  },
  {
    id: 4,
    name: "Carasadfassa",
    url: "Asesoria",
    tooltipText: "Córdoba",
    imgUrl: "./images/logos-camaras/LOGO.png",
  },
];

window.onload = init;

const renderChambers = () => {
  const chamberHtmlList = document.getElementById("chambers-items-container");
  chambersArrayMock.map((chamber) => {
    const chamberItem = document.createElement("li");
    chamberItem.classList.add("chambers-list-item");
    chamberItem.classList.add("tooltip");

    const chamberLogo = document.createElement("img");
    chamberLogo.src = chamber.imgUrl;
    chamberLogo.alt = chamber.name;
    chamberLogo.height = "150";
    chamberLogo.width = "150";

    const chamberToolText = document.createElement("span");
    chamberToolText.classList.add("tooltiptext");

    chamberToolText.appendChild(document.createTextNode(chamber.tooltipText));

    const chamberButton = document.createElement("a");
    chamberButton.href = chamber.url;

    chamberButton.appendChild(chamberLogo);
    chamberButton.appendChild(chamberToolText);

    chamberItem.appendChild(chamberButton);
    chamberHtmlList.appendChild(chamberItem);
  });
};

function init() {
  renderChambers();
}
