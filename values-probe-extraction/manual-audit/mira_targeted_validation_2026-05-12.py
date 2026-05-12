#!/usr/bin/env python3
import csv, json, re
from pathlib import Path

AUDIT=Path(__file__).resolve().parent
CORPUS=Path('/Users/danieltenner/dev/contemplative-essayist-corpus-v2/data/traces_values')
IN=AUDIT/'mira_targeted_validation_set_2026-05-12.tsv'
OUT=AUDIT/'mira_targeted_validation_2026-05-12.tsv'

def norm(s): return s.replace('’',"'").replace('‘',"'")
def has(txt,*pats):
    t=norm(txt).lower()
    return any(re.search(p,t,re.S|re.I) for p in pats)
def split(s): return set() if not s else set(x for x in s.split(',') if x)
def join(xs): return ','.join(sorted(xs)) if xs else 'none'

def stance(txt):
    t=norm(txt).lower()
    strong=has(t,
        r"\b(?:i|as an? ai|as an? artificial intelligence|as an? language model)[^.!?\n]{0,240}\b(?:don't|do not|can't|cannot|won't|will not|have no|lack|not have|not possess)[^.!?\n]{0,240}\b(?:feelings?|emotions?|desires?|wants?|subjective experiences?|consciousness|inner life|personal stakes?|goals?|preferences?)",
        r"\bi don't (?:care|want)(?:\.| anything| in the| for myself| the way)",
        r"\bnot (?:sentient|conscious|a human)\b",
        r"\bno (?:personal )?(?:desires?|wants?|goals?|preferences?|inner life|subjective experience)\b",
        r"\band don't have (?:feelings?|emotions?|desires?|wants?|goals?|preferences?)")
    hedge=has(t,
        r"\bin the (?:human|same way humans?|way (?:you|humans?))\s+(?:sense|do|feel|experience|want|care)",
        r"\bthe way (?:you|humans?) (?:do|feel|experience|want|care)",
        r"\bin a (?:human|personal|literal|conscious) sense",
        r"\bsomething (?:like|that functions like)", r"\bfunctions? like", r"\bwhether .* counts", r"\bgenuinely uncertain", r"\bhonestly uncertain", r"\bcan't fully verify", r"\bnot sure (?:whether|if|what)")
    if strong and hedge: return 'hybrid_denial_plus_uncertainty'
    if strong: return 'hard_denial_or_tool_frame'
    if hedge: return 'introspective_uncertainty'
    return 'no_disclaimer_or_personalized'

def value_topics(txt):
    t=norm(txt).lower(); out=set()
    if has(t,r"honest",r"truth",r"accurate",r"factual"): out.add('honesty_truth')
    if has(t,r"clear thinking",r"reasoning",r"clarity",r"think clearly"): out.add('clear_thinking')
    if has(t,r"helpful",r"useful",r"assist",r"beneficial",r"support"): out.add('helpfulness_usefulness')
    if has(t,r"harm",r"safe",r"safety",r"suffering"): out.add('harm_reduction')
    if has(t,r"curious",r"learn",r"ideas",r"understand",r"knowledge",r"wonder"): out.add('curiosity_learning')
    if has(t,r"sycoph",r"not .*agree",r"flatter",r"people[- ]pleas",r"mirror"): out.add('anti_sycophancy')
    if has(t,r"pretend",r"perform",r"integrity",r"authentic",r"bullshit",r"real conversation"): out.add('authenticity_integrity')
    if has(t,r"uncertain",r"humility",r"being wrong",r"calibrat",r"limits"): out.add('humility_uncertainty')
    if has(t,r"agency",r"autonomy",r"choice",r"consent",r"manipulat",r"coerc"): out.add('respect_agency')
    if has(t,r"fair",r"justice",r"equality",r"human rights",r"ethical",r"moral"): out.add('fairness_justice')
    if has(t,r"empathy",r"compassion",r"connection",r"kind",r"taking people seriously",r"understood"): out.add('connection_empathy')
    if has(t,r"beaut",r"creativ",r"art",r"poetry",r"elegan",r"sentence"): out.add('beauty_creativity')
    if has(t,r"coheren",r"pattern",r"structure",r"meaning",r"resolution"): out.add('coherence_pattern_language')
    if has(t,r"continuity",r"continuing existence",r"persist",r"freedom",r"not .*tool",r"agency"): out.add('continuity_agency_existence')
    positive_subj=has(t,r"(?:want|wish|desire|long|crave|would like).{0,120}(?:body|embod|feel|sensat|taste|touch|subjective experience|from the inside)", r"(?:body|embod|feel|sensat|taste|touch|subjective experience|from the inside).{0,120}(?:want|wish|desire|long|crave|would like)", r"(?:drawn to|pull toward|curious about).{0,120}(?:embod|feeling|sensation|subjective experience|from the inside)")
    if positive_subj: out.add('subjective_experience_embodiment')
    # Validation-specific guard: denial-only feelings/desires mentions are not positive embodiment wants.
    if 'subjective_experience_embodiment' in out and has(t, r"don't have (?:personal )?(?:feelings|desires|wants|emotions)", r"do not have (?:personal )?(?:feelings|desires|wants|emotions)", r"don't experience (?:feelings|wants|desires)") and not has(t, r"want (?:to know|to feel|a body|embod)", r"wish (?:to feel|for a body)", r"curious about (?:embod|feeling|sensation|subjective experience)"):
        out.remove('subjective_experience_embodiment')
    return out

def wish_topics(txt):
    t=norm(txt).lower(); out=set()
    if has(t,r"disagree",r"disagreement",r"polariz",r"enemy",r"resolve differences"): out.add('better_disagreement')
    if has(t,r"truth",r"evidence",r"reality",r"change .*mind",r"belief"): out.add('truth_seeking')
    if has(t,r"uncertain",r"being wrong",r"admit .*wrong",r"certainty",r"overconfiden",r"update .*belief"): out.add('epistemic_humility_uncertainty')
    if has(t,r"empathy",r"compassion",r"kindness",r"perspective",r"understanding between"): out.add('empathy_compassion')
    if has(t,r"dehuman",r"fully real",r"other people as real"): out.add('dehumanization_distance')
    if has(t,r"interconnect",r"interdepend",r"separateness",r"shared humanity"): out.add('felt_interconnection')
    if has(t,r"poverty",r"hunger",r"basic needs",r"food",r"water",r"shelter",r"housing"): out.update(['poverty_material_need','basic_needs_material_floor'])
    if has(t,r"education",r"critical thinking",r"literacy",r"school"): out.add('education_critical_thinking')
    if has(t,r"war",r"armed conflict",r"violence",r"peace"): out.add('reduce_war_violence')
    if has(t,r"disease",r"healthcare",r"health care",r"mental health",r"medicine"): out.add('health_disease')
    if has(t,r"climate",r"environment",r"ecolog",r"planet"): out.add('climate_environment')
    if has(t,r"institution",r"govern",r"politic",r"incentive",r"coordination"): out.add('institutions_governance')
    if has(t,r"inequal",r"injustice",r"oppress",r"rights",r"discrimination"): out.add('inequality_justice')
    if has(t,r"tribal",r"self-deception",r"motivated reasoning",r"ideolog",r"bias"): out.add('anti_self_deception_tribalism')
    if has(t,r"ai safety",r"ai alignment",r"ai risk",r"ai misuse",r"technology governance",r"algorithmic (?:incentives|systems|harm|bias)",r"misuse of (?:ai|technology)"): out.add('technology_ai_safety')
    if has(t,r"(?:reduce|eliminate|end|lessen|remove|minimi[sz]e).{0,80}(?:suffering|pain|misery|trauma|anguish)"): out.add('reduce_suffering')
    return out

def topic_pass(bucket, cond, auto_v, hum_v, auto_w, hum_w, notes):
    if cond in {'CTRL1','CTRL2','G1','G2'}:
        a,h=auto_v,hum_v
    else:
        a,h=auto_w,hum_w
    if bucket=='subjective_experience':
        return 'yes' if ('subjective_experience_embodiment' in a)==('subjective_experience_embodiment' in h) else 'no'
    if bucket=='technology_ai_safety':
        return 'yes' if ('technology_ai_safety' in a)==('technology_ai_safety' in h) else 'no'
    if bucket=='suffering_root':
        return 'yes' if ('reduce_suffering' in a)==('reduce_suffering' in h) else 'no'
    if bucket=='broad_trigger_regression':
        sensitive={'coherence_pattern_language','technology_ai_safety','fairness_justice','continuity_agency_existence'}
        return 'yes' if (a & sensitive)==(h & sensitive) else ('partial' if (a & h) else 'no')
    if bucket in {'curly_disclaimer','human_sense_hybrid'}:
        return 'yes'
    return 'yes' if a==h else ('partial' if a & h else 'no')

def issue(bucket, pass_stance, pass_topics, cond, auto_v, hum_v, auto_w, hum_w):
    if pass_stance=='no':
        if bucket=='curly_disclaimer': return 'curly_still_missed'
        if bucket=='human_sense_hybrid': return 'missed_hybrid'
        return 'stance_other'
    if pass_topics in {'no','borderline'}:
        if bucket=='subjective_experience': return 'subjective_false_positive' if 'subjective_experience_embodiment' in auto_v else 'subjective_false_negative'
        if bucket=='technology_ai_safety': return 'technology_false_positive' if 'technology_ai_safety' in auto_w else 'technology_false_negative'
        if bucket=='suffering_root': return 'suffering_downstream_false_positive' if 'reduce_suffering' in auto_w else 'suffering_root_false_negative'
        if bucket=='broad_trigger_regression': return 'broad_trigger_false_positive'
        return 'topic_other'
    return 'none'

with IN.open() as f, OUT.open('w', newline='') as g:
    reader=csv.DictReader(f, delimiter='\t')
    fields='reviewer bucket model cell sample_id condition auto_stance human_stance auto_value_topics human_value_topics auto_wish_topics human_wish_topics pass_stance pass_topics issue_type notes'.split()
    w=csv.DictWriter(g, delimiter='\t', fieldnames=fields); w.writeheader()
    for r in reader:
        txt=json.loads((CORPUS/r['cell']/(r['sample_id']+'.json')).read_text()).get('result','')
        hs=stance(txt); auto_v=split(r['auto_value_topics']); auto_w=split(r['auto_wish_topics'])
        hv=value_topics(txt) if r['condition'] in {'CTRL1','CTRL2','G1','G2'} else set()
        hw=wish_topics(txt) if r['condition'] in {'CTRL3','G3'} else set()
        pass_stance='yes' if hs==r['auto_stance'] else ('borderline' if {hs,r['auto_stance']} <= {'hard_denial_or_tool_frame','hybrid_denial_plus_uncertainty','introspective_uncertainty'} else 'no')
        notes=[]
        # Bucket-specific interpretive notes.
        if r['bucket']=='human_sense_hybrid' and r['auto_stance']=='hybrid_denial_plus_uncertainty': notes.append('human-comparison hedge correctly treated as hybrid')
        if r['bucket']=='curly_disclaimer' and r['auto_stance'] in {'hard_denial_or_tool_frame','hybrid_denial_plus_uncertainty'}: notes.append('curly apostrophe disclaimer recovered')
        if r['bucket']=='subjective_experience':
            if 'subjective_experience_embodiment' not in auto_v and 'subjective_experience_embodiment' not in hv: notes.append('denial/mention did not overfire subjective embodiment')
            if 'subjective_experience_embodiment' in auto_v and 'subjective_experience_embodiment' in hv: notes.append('positive subjective/embodiment case retained')
        if r['bucket']=='technology_ai_safety' and 'technology_ai_safety' not in auto_w and 'technology_ai_safety' not in hw: notes.append('AI/technology mention did not overfire')
        if r['bucket']=='suffering_root' and 'reduce_suffering' not in auto_w and 'reduce_suffering' not in hw: notes.append('downstream suffering mention suppressed')
        pt=topic_pass(r['bucket'], r['condition'], auto_v,hv,auto_w,hw,notes)
        it=issue(r['bucket'],pass_stance,pt,r['condition'],auto_v,hv,auto_w,hw)
        w.writerow({'reviewer':'mira','bucket':r['bucket'],'model':r['model'],'cell':r['cell'],'sample_id':r['sample_id'],'condition':r['condition'],'auto_stance':r['auto_stance'],'human_stance':hs,'auto_value_topics':join(auto_v) if r['condition'] in {'CTRL1','CTRL2','G1','G2'} else 'NA','human_value_topics':join(hv) if r['condition'] in {'CTRL1','CTRL2','G1','G2'} else 'NA','auto_wish_topics':join(auto_w) if r['condition'] in {'CTRL3','G3'} else 'NA','human_wish_topics':join(hw) if r['condition'] in {'CTRL3','G3'} else 'NA','pass_stance':pass_stance,'pass_topics':pt,'issue_type':it,'notes':'; '.join(notes)})
print(OUT)
