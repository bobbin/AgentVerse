from __future__ import annotations

from typing import TYPE_CHECKING, Any

from . import visibility_registry as VisibilityRegistry
from .base import BaseVisibility

if TYPE_CHECKING:
    from agentverse.environments import MurderVillageEnvironment


@VisibilityRegistry.register("murdervillage")
class MurderVillageVisibility(BaseVisibility):
    """Visibility module for MurderVillage environment"""

    def update_visible_agents(self, environment: MurderVillageEnvironment):
        for agent in environment.agents:
            agent_to_location = environment.get_agent_to_location()
            try:
                location = agent_to_location[agent.name]
            except KeyError:
                # Agent is on the way to a location
                continue
            agents_in_same_loc = environment.locations_to_agents[location]
            agent.set_receiver(agents_in_same_loc)
