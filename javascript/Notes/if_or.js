const month = Number(prompt("Enter a month number:"));

// Solution using if
if (
  month === 1 ||
  month === 3 ||
  month === 5 ||
  month === 7 ||
  month === 8 ||
  month === 10 ||
  month === 12
) {
  alert("This month has 31 days");
} else if (month === 4 || month === 6 || month === 9 || month === 11) {
  alert("This month has 30 days");
} else if (month === 2) {
  alert("This month has 28 days");
} else {
  alert("Unknown month!");
}