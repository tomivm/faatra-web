const linksArrayMock = [
  {
    id: 0,
    name: "Carassa",
    url: "https://www.youtube.com/watch?v=V2OCXiubvr0",
    tooltipText: "Turbodina",
    imgUrl: "./../images/enlaces/turbodina-logo.jpeg",
  },
  {
    id: 1,
    name: "fasfasa",
    url: "https://www.ypf.com",
    tooltipText: "YPF",
    imgUrl: "./../images/enlaces/YPF-logo.png",
  },
  {
    id: 2,
    name: "asdaddas",
    url: "Asesoria",
    tooltipText: "Taller Actual",
    imgUrl: "./../images/enlaces/TA-logo.jpg",
  },
  {
    id: 3,
    name: "Carasadfassa",
    url: "Asesoria",
    tooltipText: "Córdoba",
    imgUrl: "./../images/enlaces/Bosch-Logo.png",
  },
  {
    id: 4,
    name: "Carasadfassa",
    url: "Asesoria",
    tooltipText: "Córdoba",
    imgUrl: "./../images/enlaces/dayco-vector-logo.png",
  },
  {
    id: 5,
    name: "Carasadfassa",
    url: "Asesoria",
    tooltipText: "Córdoba",
    imgUrl: "./../images/enlaces/ngk-Logo.png",
  },
  {
    id: 6,
    name: "Carasadfassa",
    url: "Asesoria",
    tooltipText: "Córdoba",
    imgUrl: "./../images/enlaces/Motul-logo.jpg",
  },
];

window.onload = init;

const renderlinks = () => {
  const linkHtmlList = document.getElementById("links-items-container");
  linksArrayMock.map((link) => {
    const linkItem = document.createElement("li");
    linkItem.classList.add("chambers-list-item");
    linkItem.classList.add("tooltip");

    const linkLogo = document.createElement("img");
    linkLogo.src = link.imgUrl;
    linkLogo.alt = link.name;
    linkLogo.height = "150";
    linkLogo.width = "150";

    const linkToolText = document.createElement("span");
    linkToolText.classList.add("tooltiptext");

    linkToolText.appendChild(document.createTextNode(link.tooltipText));

    const linkButton = document.createElement("a");
    linkButton.target = "_blank";
    linkButton.href = link.url;

    linkButton.appendChild(linkLogo);
    linkButton.appendChild(linkToolText);

    linkItem.appendChild(linkButton);
    linkHtmlList.appendChild(linkItem);
  });
};

function init() {
  renderlinks();
}
