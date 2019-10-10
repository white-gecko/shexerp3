from shexer.io.graph.yielder.base_triples_yielder import BaseTriplesYielder
from shexer.consts import RDF_TYPE


class SgraphFromSelectorsTripleYielder(BaseTriplesYielder):

    def __init__(self, shape_map, depth=1, classes_at_last_level=True, instantiation_property=RDF_TYPE,
                 strict_syntaax_with_corners=False):
        super().__init__()
        self._shape_map = shape_map
        self._depth = depth
        self._classes_at_last_level = classes_at_last_level
        self._instantiation_property = instantiation_property
        self._strict_syntax_with_corners = strict_syntaax_with_corners


    def yield_triples(self):
        target_nodes = self._collect_every_target_node()
        sgraph = self._shape_map.get_sgraph()
        for a_triple in self._yield_relevant_sgraph_triples(target_nodes, sgraph):
            yield a_triple


    def _collect_every_target_node(self):
        result = set()
        for an_item in self._shape_map.yield_items():
            for a_node in an_item.node_selector.get_target_nodes():
                result.add(a_node)
        return list(result)


    def _yield_relevant_sgraph_triples(self, target_nodes, sgraph):
        for a_triple in sgraph.yield_p_o_triples_of_target_nodes(target_nodes=target_nodes,
                                                                 depth=self._depth,
                                                                 classes_at_last_level=self._classes_at_last_level,
                                                                 instantiation_property=self._instantiation_property,
                                                                 already_visited=None,
                                                                 strict_syntax_with_uri_corners=self._strict_syntax_with_corners):
            yield a_triple







