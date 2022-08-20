_class = """

.flaticon-001-swing
Author: Freepik

.flaticon-002-bricks
Author: Freepik

.flaticon-003-feeding-bottle
Author: Freepik

.flaticon-004-balloons
Author: Freepik

.flaticon-005-marker
Author: Freepik

.flaticon-006-spinning-top
Author: Freepik

.flaticon-007-sandbox
Author: Freepik

.flaticon-008-tambourine
Author: Freepik

.flaticon-009-bib
Author: Freepik

.flaticon-010-slide
Author: Freepik

.flaticon-011-mat
Author: Freepik

.flaticon-012-kite
Author: Freepik

.flaticon-013-brush
Author: Freepik

.flaticon-014-blackboard
Author: Freepik

.flaticon-015-potty
Author: Freepik

.flaticon-016-apple
Author: Freepik

.flaticon-017-toy-car
Author: Freepik

.flaticon-018-ball
Author: Freepik

.flaticon-019-pencil
Author: Freepik

.flaticon-020-rattle
Author: Freepik

.flaticon-021-juice-box
Author: Freepik

.flaticon-022-drum
Author: Freepik

.flaticon-023-girl
Author: Freepik

.flaticon-024-shape-toy
Author: Freepik

.flaticon-025-sandwich
Author: Freepik

.flaticon-026-paper-boat
Author: Freepik

.flaticon-027-xylophone
Author: Freepik

.flaticon-028-kindergarten
Author: Freepik

.flaticon-029-clock
Author: Freepik

.flaticon-030-crayons
Author: Freepik

.flaticon-031-bell
Author: Freepik

.flaticon-032-book
Author: Freepik

.flaticon-033-blocks
Author: Freepik

.flaticon-034-popsicle
Author: Freepik

.flaticon-035-table
Author: Freepik

.flaticon-036-boy
Author: Freepik

.flaticon-037-toys
Author: Freepik

.flaticon-038-locker
Author: Freepik

.flaticon-039-seesaw
Author: Freepik

.flaticon-040-puzzle
Author: Freepik

.flaticon-041-abacus
Author: Freepik

.flaticon-042-synthesizer
Author: Freepik

.flaticon-043-teddy-bear
Author: Freepik

.flaticon-044-scissors
Author: Freepik

.flaticon-045-cookies
Author: Freepik

.flaticon-046-bucket
Author: Freepik

.flaticon-047-backpack
Author: Freepik

.flaticon-048-paper-plane
Author: Freepik

.flaticon-049-cutlery
Author: Freepik

.flaticon-050-fence
Author: Freepik

"""



# new_w = []
# for w in _class.split('\n'):
#     if len(w) != 0 and w[0] == '.':
#         tmp = w.split('-', maxsplit=1)
#         print(f'("{w[1:]}", "{tmp[-1]}"),')
#         # new_w.append(tmp[-1])


# primary
# secondary
# success
# danger
# warning
# info
# light
# dark

s = """
 'aaggregate', 'abulk_create', 'abulk_update', 'acontains', 'acount', 'acreate', 'adelete', 'aearliest', 'aexists', 'aexplain', 'afirst', 'aget', 'aget_or_
create', 'aggregate', 'ain_bulk', 'aiterator', 'alast', 'alatest', 'alias', 'all', 'annotate', 'as_manager', 'aupdate', 'aupdate_or_create', 'bulk_create', 'bulk_update', 'complex_filter', 'contains', 'count', 'create', 'dates', 'datet
imes', 'db', 'defer', 'delete', 'difference', 'distinct', 'earliest', 'exclude', 'exists', 'explain', 'extra', 'filter', 'first', 'get', 'get_or_create', 'in_bulk', 'intersection', 'iterator', 'last', 'latest', 'model', 'none', 'only',
 'order_by', 'ordered', 'prefetch_related', 'query', 'raw', 'resolve_expression', 'reverse', 'select_for_update', 'select_related', 'union', 'update', 'update_or_create', 'using', 'values', 'values_list'
"""

s.replace('\'', '')
print(s)
