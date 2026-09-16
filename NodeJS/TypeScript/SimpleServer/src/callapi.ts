// Functions to make requests to the swapi.info API.
export async function callApi<T>(resource: string): Promise<T> {
	const response = await fetch(`https://swapi.info/api/${resource}`);

	if (!response.ok) {
		throw new Error(`SWAPI request failed: ${response.status} ${response.statusText}`);
	}

	return response.json() as Promise<T>;
}