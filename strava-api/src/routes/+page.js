import { redirect } from '@sveltejs/kit';

export const load = async ({ fetch, parent }) => {
    const {user} = await parent();
    if(!user) {
        throw redirect(302, '/login');
    }   
    const records = await fetch(`http://localhost:8000/${user?.id}/records`);
  
    const recordsRes = await records;
    const recordsData = recordsRes.ok ? await recordsRes.json() : undefined;
    return {
        records: recordsData
    };
  };
  