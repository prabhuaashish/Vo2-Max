import {error} from '@sveltejs/kit';

export const load = async ({fetch, params}) => {
    const raceRecordRes = await fetch(`http://localhost:8000/race-records/${params.id}`);

    if(!raceRecordRes.ok){
        throw error(raceRecordRes.status, 'Failed to load activity!');
    }

    const raceRecordJSON = await raceRecordRes.json();

    return {
        race_record: raceRecordJSON,
    }
}