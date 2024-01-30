const theme = localStorage.getItem("THEME");

if (theme) {
  if (theme === "LIGHT") {
    document.querySelector("html").setAttribute("data-theme", "LIGHT");
  } else {
    document.querySelector("html").setAttribute("data-theme", "DARK");
  }
} else {
  document.querySelector("html").setAttribute("data-theme", "LIGHT");
  localStorage.setItem("THEME", "LIGHT");
}
