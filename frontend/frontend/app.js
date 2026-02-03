async function getEvents() {
  const location = document.getElementById('location').value;
  const interest = document.getElementById('interest').value;

  const response = await fetch(
    `https://api-id.execute-api.region.amazonaws.com/events?location=${location}&interest=${interest}`
  );

  const data = await response.json();
  document.getElementById('events').innerHTML =
    JSON.stringify(data, null, 2);
}
