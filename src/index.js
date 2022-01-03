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
