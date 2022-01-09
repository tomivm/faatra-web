const mockTrainingItem = {
  id: 1,
  url: "https://www.facebook.com",
  title: "Capacitación de inyección directa de gasolina",
  description:
    "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nesciunt hic atque dicta illo natus dolore cupiditate exercitationem dolorum recusandae, unde voluptatum sequi animi expedita voluptas porro omnis repellendus. Ab suscipit doloribus porro libero assumenda deleniti tenetur quisquam asperiores, dignissimos quibusdam?",
};

const mockTrainingList = Array(9)
  .fill()
  .map(() => mockTrainingItem);

console.log("mockTrainingList", mockTrainingList);

//----------------------------------------------------------------------

const trainingList = mockTrainingList;

const filteredTrainingList = trainingList;

const actualPage = 1;

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

const TotalPages = getPages(filteredTrainingList);

const trainingListActualPage = getTrainingListActualPage(
  actualPage,
  filteredTrainingList
);

console.log("TrainingListActualPage", trainingListActualPage);

window.onload = init;

//-----------------------------------------------------------------

function changePage(pageNumber) {
  const trainingListActualPage = getTrainingListActualPage(
    pageNumber,
    filteredTrainingList
  );
  showActualPage(trainingListActualPage);
}

function init() {
  changePage(1);
}

function showActualPage(trainingListActualPage) {
  const trainingItemsContainer = document.getElementById(
    "training-form-items-id"
  );

  const trainingItems = [
    ...trainingItemsContainer.getElementsByClassName("training-list-item"),
  ];

  const modifyHTML = () =>
    trainingItems.map((trainingItem, index) => {
      console.log("hola");
      if (!trainingListActualPage[index]) {
        trainingItem.style.display = "none";
        return;
      }
      const { title, description, url } = trainingListActualPage[index];
      trainingItem.getElementsByTagName("H2")[0].innerHTML = title;
      trainingItem.getElementsByTagName("P")[0].innerHTML = description;
      trainingItem.setAttribute("href", url);
    });

  modifyHTML();
}

const createTrainingItem = ({ title, description, url }) => {
  const trainingItem = document.createElement("a");
  trainingItem.classList.add("training-list-item", "inclusion-bg");

  const createTitleContainer = () => {
    const titleContainer = document.createElement("div");
    titleContainer.classList.add("training-list-item-tittle-container");

    const h2 = document.createElement("h2");
    const titleTextNode = document.createTextNode(title); // Create a text node
    h2.appendChild(titleTextNode); // Append the text to <h1>

    titleContainer.appendChild(h2);

    const buttonContainer = document.createElement("div");
    buttonContainer.classList.add("primary-btn-container");

    const button = document.createElement("button");
    button.classList.add("primary-btn", "btn-sm", "more-info-btn");

    buttonContainer.appendChild(button);
    titleContainer.appendChild(buttonContainer);
    return titleContainer;
  };

  const createDescription = () => {
    const description = document.createElement("div");
    description.classList.add("training-list-item-description");
    description.appendChild(document.createElement("p"));
    return description;
  };

  trainingItem.appendChild(createTitleContainer());
  trainingItem.appendChild(createDescription());

  console.log("trainingItem", trainingItem);
};

{
  /* <a class="training-list-item inclusion-bg">
  <div class="training-list-item-tittle-container">
    <h2>Capacitación de inyección directa de gasolina</h2>
    <div class="primary-btn-container">
      <div class="primary-btn btn-sm more-info-btn">+ info</div>
    </div>
  </div>
  <div class="training-list-item-description">
    <p>
      Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias, fuga.
    </p>
  </div>
</a>; */
}
