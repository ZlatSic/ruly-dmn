import abc


class ModelHandler(abc.ABC):
    """Abstract class representing a connection between an encoded DMN model
    and ruly's rules. Implementation should parse initial rules from the model
    and be available for updates with new rules."""

    @abc.abstractproperty
    @property
    def dependencies(self):
        """Dict[Tuple(str), Tuple(str)]: output-input variable name pairs"""

    @abc.abstractproperty
    @property
    def rules(self):
        """List[ruly.Rule]: all rules available in the model"""
        return self._rules

    @abc.abstractmethod
    def update(self, knowledge_base):
        """Updates handler with a new knowledge base

        Args:
            knowledge_base (ruly.KnowledgeBase): new knowledge base
        """


class RuleFactory(abc.ABC):
    """Abstract class whose instances should implement rule creation methods"""

    @abc.abstractmethod
    def create_rule(self, state, fired_rules, output_names):
        """Creates a new rule

        Args:
            state (Dict[str, Any]): state
            fired_rules (List[ruly.Rule]): rules activated for state and output
                combination
            output_names (Tuple[str]): output values for the new rule's
                consequent

        Returns:
            Optional[ruly.Rule]: generated rule, if None, new rule couldn't be
            created with given inputs"""
