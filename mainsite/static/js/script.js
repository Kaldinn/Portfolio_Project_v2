function smoothScroll(event, target) {
    event.preventDefault(); // Zapobiega domyślnemu odświeżaniu strony
    const element = document.querySelector(target);
    window.scrollTo({
      top: element.offsetTop,
      behavior: 'smooth'
    });
  }

  function openCV(){
    window.open("/mainsite/static/cv/DanielSkulimowski-Eng-CV.pdf")
  }