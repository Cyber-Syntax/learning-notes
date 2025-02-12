//const unixTimestampInSeconds = 1734432453615; // with timezone
const unixTimestampInSeconds = 1734432827921; // without TZ:timezone
const date = new Date(unixTimestampInSeconds * 1000); // Convert to milliseconds
console.log(date.toString()); // Convert the timestamp to a readable date format
