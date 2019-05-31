
class NodeSelector(object):

    def __init__(self, raw_selector, sgraph):
        self._raw_selector = raw_selector
        self._sgraph = sgraph

    def get_target_nodes(self):
        """
        It return a list of target URIs. It may require to execute some query against a given endpoint

        :return:
        """
        raise NotImplementedError()

    def yield_graph_of_target_nodes(self, depth=1, classes_for_last_level=True):
        for a_triple in self._sgraph:  # TODO! Call the method commented
            pass

            # yield_p_o_triples_of_target_nodes(self, target_nodes, depth, classes_at_last_level=True,
            #                                   instantiation_property=None, already_visited=None):

    @property
    def raw_selector(self):
        return self._raw_selector


########################################################


class NodeSelectorNoSparql(NodeSelector):

    def __init__(self, raw_selector, sgraph, target_node):
        super().__init__(raw_selector=raw_selector, sgraph=sgraph)
        self._target_nodes = [target_node]

    def get_target_nodes(self):
        return self._target_nodes


########################################################



class NodeSelectorSparql(NodeSelector):

    def __init__(self, raw_selector, sgraph, sparql_query_selector, id_variable_query):
        super().__init__(raw_selector=raw_selector, sgraph=sgraph)
        self._sparql_query_selector = sparql_query_selector
        self._id_variable_query = id_variable_query
        self._target_nodes = None

    @property
    def sparql_query_selector(self):
        return self._sparql_query_selector

    def get_target_nodes(self):
        if self._target_nodes is None:
            self._target_nodes = self._solve_target_nodes_at_endpoint()
        return self._target_nodes



    def _solve_target_nodes_at_endpoint(self):
        return self._sgraph.query_single_variable(str_query=self._sparql_query_selector,
                                                  variable_id=self._id_variable_query)



