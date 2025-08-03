"""
semantic_routing_tests.py

Tests the LVCS routing pipeline for correctness under varied polarity, archetype, and zone configurations.
Ensures SPLs are routed into appropriate zones and release protocols behave as expected.
"""

import unittest
from modules.LVCFATE.fate_balancer import generate_fate_balance_chart
from modules.LVCEDRA_GraceBeauty.archetype_mapper import generate_archetype_mapping
from modules.LVCS.lvcs_orchestrator import orchestrate_routing
from modules.LVCS.release_protocols import cleanse_overflow_zones

class TestSemanticRouting(unittest.TestCase):

    def setUp(self):
        self.planet_positions = {
            'Mars': ('Aries', 18.5),
            'Saturn': ('Capricorn', 3.2),
            'Moon': ('Cancer', 22.1)
        }

        self.spl_overlay = {
            'SPL-001': ['Mars', 'Moon'],
            'SPL-002': ['Saturn'],
            'SPL-038': ['Mars'],
            'SPL-044': ['Moon']
        }

        self.modulation_zones = [
            {'zone_id': 'Z01', 'archetype': 'Imprinting', 'polarity_absorption': 0.65, 'capacity': 10},
            {'zone_id': 'Z12', 'archetype': 'Constraint', 'polarity_absorption': 0.9, 'capacity': 15}
        ]

        self.zone_metadata = {
            'SPL-038': {'ritual_protocol': 'Iron Diffusion'},
            'SPL-044': {'ritual_protocol': 'Flame Invocation'}
        }

    def test_routing_integrity(self):
        output = orchestrate_routing(self.planet_positions, self.spl_overlay, self.modulation_zones)
        self.assertIn('RoutingPlan', output)
        self.assertIn('SPL-001', output['RoutingPlan'])
        self.assertIsInstance(output['RoutingPlan'], dict)

    def test_release_protocols(self):
        fate_chart = generate_fate_balance_chart(self.planet_positions, self.spl_overlay)
        routing_plan = {
            'SPL-038': 'OverflowZone',
            'SPL-044': 'OverflowZone',
            'SPL-001': 'Z01',
            'SPL-002': 'Z12'
        }
        released = cleanse_overflow_zones(routing_plan, fate_chart['BufferedSPLs'], self.zone_metadata)
        self.assertAlmostEqual(released['SPL-038'], round(fate_chart['BufferedSPLs']['SPL-038'] * 0.8, 2))
        self.assertAlmostEqual(released['SPL-044'], round(fate_chart['BufferedSPLs']['SPL-044'] * 0.75, 2))

if __name__ == '__main__':
    unittest.main()
