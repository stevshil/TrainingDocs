import {useParams} from 'react-router';
import { searchPeople } from './types/Person';
import {people} from './data/People';


function Home2() {
    const params = useParams();
    let uname: string;
    uname = params.name;
    let chosenone = searchPeople(people,"name",uname)[0];

    return (
        <>
            <h1>HOME 2</h1>
            <h3>Welcome {chosenone.name}</h3>
            <p>Age: {chosenone.age}</p>
            <p>Hobby of {chosenone.hobby}</p>
        </>
    )
};

export default Home2;