import fetchRefresh from '$lib/helpers/fetch-refresh.js';
import {error} from '@sveltejs/kit';

export const load = async ({fetch, params}) => {
    const activityRes = await fetchRefresh(fetch, `/api/strava/activities/${params.id}`);

    if(!activityRes.ok){
        throw error(activityRes.status, 'Failed to load activity!');
    }

    const activityJSON = await activityRes.json();

    return {
        activity: activityJSON,
        title: activityJSON.name
    }
}