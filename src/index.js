function openMenu() {
  const isOpenClass = () => {
    const open = () => {
      navbarContainer.classList.add("navbar-container-open");
      console.log(navbarBackground);
      navbarBackground.style.display = "block";
    };

    const close = () => {
      navbarContainer.classList.remove("navbar-container-open");
      navbarBackground.style.display = "none";
    };

    const navbarContainer = document.getElementById("navbar-container");
    const navbarBackground = document.getElementById("nav-background");

    if (navbarContainer.classList.contains("navbar-container-open"))
      return close();
    return open();
  };

  isOpenClass();

  const navbarItems = document.getElementsByClassName("navbar-item");
  const navbarItemsArray = Array.prototype.slice.call(navbarItems);
  navbarItemsArray.forEach((item) => {
    if (item.classList.contains("show-navbar-item"))
      return item.classList.remove("show-navbar-item");
    item.classList.add("show-navbar-item");
    // if (item.style.display !== "block") return (item.style.display = "block");
    // return (item.style.display = "none");
  });
}

function openInscriptForm() {
  const isOpenClass = () => {
    const open = () => {
      body.classList.add("disable-scroll");
      modalForm.classList.add("modal-form");
      modalBackground.style.display = "grid";
    };

    const close = () => {
      modalForm.classList.remove("modal-form");
      modalBackground.style.display = "none";
      body.classList.remove("disable-scroll");
    };

    const body = document.body;
    const modalForm = document.getElementById("inscription-form");
    const modalBackground = document.getElementById("inscription-form-bg");

    if (modalForm.classList.contains("modal-form")) return close();
    return open();
  };

  isOpenClass();
}
