const mockTrainingItem = {
  id: 1,
  provincia: "Córdoba",
  camara: "Camara1",
  especialidad: "Electrónica",
  url: "./capacitacion-full.html",
  title: "Capacitación de inyección directa de gasolina",
  description:
    "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nesciunt hic atque dicta illo natus dolore cupiditate exercitationem dolorum recusandae, unde voluptatum sequi animi expedita voluptas porro omnis repellendus. Ab suscipit doloribus porro libero assumenda deleniti tenetur quisquam asperiores, dignissimos quibusdam?",
  backgroundImageURL: "./images/capacitacion/calculadora-y-hojas.jpg",
};

const mockTrainingItemDifferent = {
  id: 1,
  provincia: "Córdoba",
  camara: "Camara2",
  especialidad: "Electrónica",
  url: "./capacitacion-full.html",
  title: "Capacitación de restauracion",
  description:
    "tus dolore cupiditate exercitationem dolorum ecusandae, unde voluptatum sequi animi expedita voluptas porro omnis repellendus. Ab suscipit doloribus porro libero assumenda deleniti tenetur quisquam asperiores, dignissimos quibusdam?",
  backgroundImageURL: "./images/capacitacion/calculadora-y-hojas.jpg",
};

const mockTrainingList = Array(27)
  .fill()
  .map(() => mockTrainingItem);

//----------------------------------------------------------------------
mockTrainingList.push(mockTrainingItemDifferent);
const trainingList = mockTrainingList;

const provinceOptions = ["Córdoba", "Rosario", "Tierra Del Fuego", "Salta"];
const chambersOptions = ["Camara1", "Camara2", "Camara3"];
const specialtiesOptions = ["Mecanica", "Electrónica", "Pintura"];

const PROVINCE_ID = "province-select";
const CHAMBER_ID = "chamber-select";
const SPECIALTY_ID = "specialty-select";

let filteredTrainingList = trainingList;

function getPages(filteredTrainingList) {
  const PAGE_MAX_ITEMS = 6;
  return Math.ceil(filteredTrainingList.length / PAGE_MAX_ITEMS);
}

const getTrainingListActualPage = (actualPage, filteredTrainingList) => {
  const PAGE_MAX_ITEMS = 6;
  return filteredTrainingList.slice(
    (actualPage - 1) * PAGE_MAX_ITEMS,
    actualPage * PAGE_MAX_ITEMS
  );
};

const trainingPageState = {
  actualPage: 1,
  totalPages: getPages(filteredTrainingList),
};

const trainingListActualPage = getTrainingListActualPage(
  trainingPageState.actualPage,
  filteredTrainingList
);

window.onload = init;

function addSelectsOptions() {
  const fillSelect = (selectId, options) => {
    const selectContainer = document.getElementById(selectId);

    const nullOption = document.createElement("option");
    nullOption.value = null;
    const nullOptionTextNode = document.createTextNode("todas");
    nullOption.appendChild(nullOptionTextNode);
    selectContainer.appendChild(nullOption);

    options.map((value) => {
      const option = document.createElement("option");
      option.value = value;
      const optionTextNode = document.createTextNode(value);
      option.appendChild(optionTextNode);

      selectContainer.appendChild(option);
    });
  };

  fillSelect(PROVINCE_ID, provinceOptions);
  fillSelect(CHAMBER_ID, chambersOptions);
  fillSelect(SPECIALTY_ID, specialtiesOptions);
}

function handleSelectChange() {
  const applyFilters = ({
    selectedProvince,
    selectedChamber,
    selectedSpecialty,
  }) => {
    const filteredList = trainingList.filter(
      (item) =>
        (item.provincia === selectedProvince || selectedProvince === "null") &&
        (item.camara === selectedChamber || selectedChamber === "null") &&
        (item.especialidad === selectedSpecialty ||
          selectedSpecialty === "null")
    );
    return filteredList;
  };

  const refreshPage = () => {
    trainingPageState.actualPage = 1;
    trainingPageState.totalPages = getPages(filteredTrainingList);
    changePage(trainingPageState);
  };

  const updateValue = (selectId) => {
    const select = document.getElementById(selectId);
    return select.options[select.selectedIndex].value;
  };

  const selectedProvince = updateValue(PROVINCE_ID);
  const selectedChamber = updateValue(CHAMBER_ID);
  const selectedSpecialty = updateValue(SPECIALTY_ID);

  filteredTrainingList = applyFilters({
    selectedProvince,
    selectedChamber,
    selectedSpecialty,
  });

  refreshPage();
}

function changePage({ actualPage, totalPages }) {
  const trainingListActualPage = getTrainingListActualPage(
    actualPage,
    filteredTrainingList
  );

  const renderActualPage = (trainingListActualPage) => {
    const createTrainingItem = ({
      title,
      description,
      url,
      backgroundImageURL,
    }) => {
      const trainingItem = document.createElement("a");
      trainingItem.classList.add(
        "training-list-item",
        "bg-img-cover",
        "scale-hover"
      );

      const createTitleContainer = () => {
        const titleContainer = document.createElement("div");
        titleContainer.classList.add("training-list-item-tittle-container");

        const h2 = document.createElement("h2");
        const titleTextNode = document.createTextNode(title);
        h2.appendChild(titleTextNode);

        titleContainer.appendChild(h2);

        const buttonContainer = document.createElement("div");
        buttonContainer.classList.add("primary-btn-container");

        const button = document.createElement("button");
        button.classList.add("primary-btn", "btn-sm", "more-info-btn");
        const buttonTextNode = document.createTextNode("+ info");
        button.appendChild(buttonTextNode);

        buttonContainer.appendChild(button);
        titleContainer.appendChild(buttonContainer);
        return titleContainer;
      };

      const createDescription = () => {
        const descriptionContainer = document.createElement("div");
        descriptionContainer.classList.add("training-list-item-description");

        const p = document.createElement("p");
        const descriptionTextNode = document.createTextNode(description); // Create a text node

        p.appendChild(descriptionTextNode);
        descriptionContainer.appendChild(p);
        return descriptionContainer;
      };

      trainingItem.appendChild(createTitleContainer());
      trainingItem.appendChild(createDescription());
      trainingItem.href = url;
      trainingItem.style.backgroundImage = `linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.76)),url(${backgroundImageURL})`;

      return trainingItem;
    };

    const trainingItemsContainer = document.getElementById(
      "training-form-items-id"
    );

    trainingItemsContainer.innerHTML = "";

    trainingListActualPage.map((trainingItem) => {
      const item = createTrainingItem(trainingItem);

      trainingItemsContainer.appendChild(item);
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

  renderActualPage(trainingListActualPage);
  renderPagesNavigator({ actualPage, totalPages });
}

function init() {
  addSelectsOptions();
  changePage(trainingPageState);
}
