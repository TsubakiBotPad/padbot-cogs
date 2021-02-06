from padinfo.core.find_monster import findMonsterCustom2
from padinfo.core.id import get_monster_misc_info


async def perform_transforminfo_query(dgcog, raw_query, beta_id3):
    db_context = dgcog.database
    mgraph = dgcog.database.graph
    m, err, debug_info = await findMonsterCustom2(dgcog, beta_id3, raw_query)
    altversions = mgraph.process_alt_versions(m.monster_id)

    for mid in sorted(altversions):
        if mgraph.monster_is_transform_base_by_id(mid):
            tfm = mgraph.get_monster(mgraph.get_next_transform_id_by_monster_id(mid))
            if tfm:
                bm = mgraph.get_monster(mid)
                break

    if not tfm:
        return m, err, debug_info, None, None, None, None # ????

    acquire_raw, _, base_rarity, _, true_evo_type_raw = await get_monster_misc_info(db_context, tfm)

    return bm, err, debug_info, tfm, base_rarity, acquire_raw, true_evo_type_raw