import { callApi } from "./callapi";
import { Film } from "../Types/Film";
import http from "http";
// lry http = require('http');

const websrv = http.createServer(async (req, res) => {
  if (req.url === "/films") {
    try {
      const films = await callApi<Film[]>("films");
      res.writeHead(200, { "Content-Type": "text/html" });
      const table = films.map(film => `
        <tr>
          <td>${film.episode_id}</td>
          <td>${film.title}</td>
          <td>${film.director}</td>
          <td>${film.release_date}</td>
        </tr>`).join("\n");

      const finaltable = `<table>
        <thead>
          <tr><th>Episode</th><th>Title</th><th>Director</th><th>Release Date</th></tr>
        </thead>
        <tbody>${table}</tbody>
      </table>`;
      
      res.end(finaltable);
    } catch (error) {
      res.writeHead(500, { "Content-Type": "text/plain" });
      res.end("Failed to fetch films");
    }
  } else {
    res.writeHead(404, { "Content-Type": "text/plain" });
    res.end("Realy not Found");
  }
});

websrv.listen(3300, () => {
  console.log("Server running at http://localhost:3300/");
});
// }).listen(3000, () => {
//   console.log("Server running at http://localhost:3000/");
// });