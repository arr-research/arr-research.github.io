from pathlib import Path
src=Path(r'C:\Trabajo\airr\2026-10-27_knowledge1028\sweep1028.py').read_text()
src=src.replace('2026-10-27_profile1011/READINGS1011.json','2026-10-27_knowledge1028/READINGS1028.json')
src=src.replace("C/'READINGS1028.json'","C/'READINGS1033.json'")
src=src.replace('selected statements/proofs inSection8.1,Lemma8.1,Propositions8.2-8.4; abstract and ordinaryqubitLemma3.12; not wholepaperproofaudit','HTTP identity refreshed; selected reading from1028 reused, no new whole-paper proof audit')
src=src.replace('No results returned for the narrow search queries; not evidence that no covering theorem exists. Direct2011.05949v4passages read separately.','Historical1028 narrow queries returned none. Current1033 additional queries found primary leads1008.1557 and2204.09963, abstracts read separately; no exhaustive coverage claim.')
(Path(__file__).parent/'sweep1033.py').write_text(src,encoding='utf-8',newline='\n')
