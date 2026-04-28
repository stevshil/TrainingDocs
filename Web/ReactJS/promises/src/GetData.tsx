import { useEffect, useState } from "react";

function GetData() {

    const [data, setData] = useState<any[]>([]);

    useEffect( () => {
        let url = "https://swapi.info/api/films";

        const fetchData = async () => {
            try {
                const response = await fetch(url);

                if ( ! response.ok ) {
                    throw new Error(`HTTP error $(response.status)`);
                }

                const swapi = await response.json();

                if (swapi) {
                    setData(swapi);
                }
            } catch (e) {
                console.log(`Error ${e}`)
            }
        }

    fetchData();

    }, []);

    console.log(`Main : ${data[0]?.title}`)

    return (
        <table>
            <thead>
                <tr>
                    <th>Title</th>
                    <th>Episode</th>
                    <th>Release Date</th>
                </tr>
            </thead>
            <tbody>
                {data.map((film) => (
                    <tr key={film.episode_id}>
                        <td>{film.title}</td>
                        <td>{film.episode_id}</td>
                        <td>{film.release_date}</td>
                    </tr>
                ))}
            </tbody>
        </table>
    )
}

export default GetData;