import {error} from '@sveltejs/kit';

export const load = async ({fetch, params}) => {
    const paceRecordRes = await fetch(`http://localhost:8000/pace-records/${params.id}`);

    if(!paceRecordRes.ok){
        throw error(paceRecordRes.status, 'Failed to load activity!');
    }

    const paceRecordJSON = await paceRecordRes.json();

    return {
        pace_record: paceRecordJSON,
    }
}