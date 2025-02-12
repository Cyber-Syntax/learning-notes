const month = Number(prompt("Enter a month number:"));

// Solution using if and switch
if (month >= 1 && month <= 12) {
    let nbdays = 31;
    switch (month) {
      case 4:
      case 6:
      case 9:
      case 11:
        nbdays = 30;
        break;
      case 2:
        nbdays = 28;
        break;
    }
    alert(`This month has ${nbdays} days`);
  } else {
    alert("Unknown month!");
  }