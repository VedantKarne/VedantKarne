"""
Inject visual effects into a generated GitHub contribution snake SVG.

Usage:
    python scripts/enhance_snake.py dist/github-snake.svg
    python scripts/enhance_snake.py dist/github-snake-dark.svg --dark
"""

from __future__ import annotations

import argparse
from pathlib import Path


LIGHT_EFFECTS = """
<!-- Vedant Karne: enhanced snake effects -->
<defs>
  <!-- Soft violet neon glow -->
  <filter id="snake-neon-glow"
          x="-60%"
          y="-60%"
          width="220%"
          height="220%">
    <feGaussianBlur
      stdDeviation="2.6"
      result="softBlur"
    />

    <feColorMatrix
      in="softBlur"
      type="matrix"
      values="
        0.49 0    0    0 0
        0    0.23 0    0 0
        0    0    0.93 0 0
        0    0    0    1 0
      "
      result="violetGlow"
    />

    <feMerge>
      <feMergeNode in="violetGlow"/>
      <feMergeNode in="SourceGraphic"/>
    </feMerge>
  </filter>

  <!-- Strong glow intended for the snake head -->
  <filter id="snake-head-glow"
          x="-100%"
          y="-100%"
          width="300%"
          height="300%">
    <feGaussianBlur
      stdDeviation="4"
      result="headBlur"
    />

    <feFlood
      flood-color="#A78BFA"
      flood-opacity="0.9"
      result="headColour"
    />

    <feComposite
      in="headColour"
      in2="headBlur"
      operator="in"
      result="colouredHeadBlur"
    />

    <feMerge>
      <feMergeNode in="colouredHeadBlur"/>
      <feMergeNode in="SourceGraphic"/>
    </feMerge>
  </filter>

  <!-- Contribution-cell glow -->
  <filter id="cell-glow"
          x="-40%"
          y="-40%"
          width="180%"
          height="180%">
    <feGaussianBlur
      stdDeviation="1.2"
      result="cellBlur"
    />

    <feMerge>
      <feMergeNode in="cellBlur"/>
      <feMergeNode in="SourceGraphic"/>
    </feMerge>
  </filter>

  <!-- Gradient that can be used by supporting elements -->
  <linearGradient id="violet-energy-gradient"
                  x1="0%"
                  y1="0%"
                  x2="100%"
                  y2="100%">
    <stop offset="0%" stop-color="#DDD6FE"/>
    <stop offset="45%" stop-color="#A78BFA"/>
    <stop offset="75%" stop-color="#7C3AED"/>
    <stop offset="100%" stop-color="#4C1D95"/>
  </linearGradient>
</defs>

<style>
  /*
   * Primary snake glow.
   * The selectors are intentionally broad because generated snk SVG
   * structures may differ between releases.
   */
  svg g[style*="transform"],
  svg g[id*="snake"],
  svg g[class*="snake"] {
    filter: url(#snake-neon-glow);
  }

  /*
   * Smooth breathing effect.
   * Uses opacity and filter intensity instead of large scaling,
   * preventing the animation from looking jumpy.
   */
  svg {
    animation: snakeSceneFade 1.1s ease-out both;
  }

  svg rect {
    transform-box: fill-box;
    transform-origin: center;
  }

  /*
   * Contribution squares subtly brighten.
   * Keep the effect restrained so the snake remains the focal point.
   */
  svg rect:not([fill="none"]) {
    animation: contributionBreath 4.8s ease-in-out infinite;
  }

  /*
   * Offset animation timings create a wave rather than making all
   * contribution cells pulse simultaneously.
   */
  svg rect:nth-of-type(3n) {
    animation-delay: -0.8s;
  }

  svg rect:nth-of-type(4n) {
    animation-delay: -1.6s;
  }

  svg rect:nth-of-type(5n) {
    animation-delay: -2.4s;
  }

  svg rect:nth-of-type(7n) {
    animation-delay: -3.2s;
  }

  @keyframes snakeSceneFade {
    from {
      opacity: 0;
      transform: translateY(4px);
    }

    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  @keyframes contributionBreath {
    0%,
    100% {
      opacity: 0.82;
      filter: brightness(0.95);
    }

    50% {
      opacity: 1;
      filter: brightness(1.16);
    }
  }

  /*
   * Accessibility: viewers requesting reduced motion get the normal
   * snake movement without the additional pulsing layer.
   */
  @media (prefers-reduced-motion: reduce) {
    svg,
    svg rect {
      animation: none !important;
    }
  }
</style>
"""


DARK_EFFECTS = """
<!-- Vedant Karne: enhanced dark-mode snake effects -->
<defs>
  <filter id="snake-neon-glow"
          x="-70%"
          y="-70%"
          width="240%"
          height="240%">
    <feGaussianBlur
      stdDeviation="3"
      result="softBlur"
    />

    <feFlood
      flood-color="#8B5CF6"
      flood-opacity="0.95"
      result="glowColour"
    />

    <feComposite
      in="glowColour"
      in2="softBlur"
      operator="in"
      result="colouredGlow"
    />

    <feMerge>
      <feMergeNode in="colouredGlow"/>
      <feMergeNode in="colouredGlow"/>
      <feMergeNode in="SourceGraphic"/>
    </feMerge>
  </filter>

  <filter id="cell-glow"
          x="-45%"
          y="-45%"
          width="190%"
          height="190%">
    <feGaussianBlur
      stdDeviation="1.5"
      result="cellBlur"
    />

    <feFlood
      flood-color="#7C3AED"
      flood-opacity="0.45"
      result="cellColour"
    />

    <feComposite
      in="cellColour"
      in2="cellBlur"
      operator="in"
      result="colouredCellBlur"
    />

    <feMerge>
      <feMergeNode in="colouredCellBlur"/>
      <feMergeNode in="SourceGraphic"/>
    </feMerge>
  </filter>

  <radialGradient id="ambient-violet-glow">
    <stop offset="0%" stop-color="#7C3AED" stop-opacity="0.24"/>
    <stop offset="55%" stop-color="#4C1D95" stop-opacity="0.10"/>
    <stop offset="100%" stop-color="#05050A" stop-opacity="0"/>
  </radialGradient>
</defs>

<style>
  svg {
    animation: sceneEntrance 1.2s cubic-bezier(0.22, 1, 0.36, 1) both;
  }

  svg g[style*="transform"],
  svg g[id*="snake"],
  svg g[class*="snake"] {
    filter: url(#snake-neon-glow);
  }

  svg rect {
    transform-box: fill-box;
    transform-origin: center;
  }

  svg rect:not([fill="none"]) {
    animation: darkCellPulse 5.2s ease-in-out infinite;
  }

  svg rect:nth-of-type(3n) {
    animation-delay: -1s;
  }

  svg rect:nth-of-type(4n) {
    animation-delay: -2s;
  }

  svg rect:nth-of-type(5n) {
    animation-delay: -3s;
  }

  svg rect:nth-of-type(6n) {
    animation-delay: -4s;
  }

  @keyframes sceneEntrance {
    0% {
      opacity: 0;
      transform: translateY(6px);
      filter: blur(3px);
    }

    60% {
      opacity: 1;
      filter: blur(0);
    }

    100% {
      opacity: 1;
      transform: translateY(0);
      filter: blur(0);
    }
  }

  @keyframes darkCellPulse {
    0%,
    100% {
      opacity: 0.72;
      filter: brightness(0.9);
    }

    50% {
      opacity: 1;
      filter:
        brightness(1.28)
        drop-shadow(0 0 2px rgba(139, 92, 246, 0.42));
    }
  }

  @media (prefers-reduced-motion: reduce) {
    svg,
    svg rect {
      animation: none !important;
    }
  }
</style>
"""


def inject_effects(svg_content: str, effects: str) -> str:
    """Insert the effects immediately after the opening SVG tag."""

    if "Vedant Karne: enhanced" in svg_content:
        print("Effects already exist. Skipping duplicate injection.")
        return svg_content

    opening_tag_end = svg_content.find(">")

    if opening_tag_end == -1:
        raise ValueError("The file does not contain a valid opening SVG tag.")

    return (
        svg_content[: opening_tag_end + 1]
        + "\n"
        + effects
        + "\n"
        + svg_content[opening_tag_end + 1 :]
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Add glow and transition effects to a snake SVG."
    )

    parser.add_argument(
        "svg_path",
        type=Path,
        help="Path to the generated SVG file.",
    )

    parser.add_argument(
        "--dark",
        action="store_true",
        help="Use the stronger dark-mode effect palette.",
    )

    args = parser.parse_args()

    if not args.svg_path.exists():
        raise FileNotFoundError(f"SVG not found: {args.svg_path}")

    original_svg = args.svg_path.read_text(encoding="utf-8")
    selected_effects = DARK_EFFECTS if args.dark else LIGHT_EFFECTS

    enhanced_svg = inject_effects(
        svg_content=original_svg,
        effects=selected_effects,
    )

    args.svg_path.write_text(
        enhanced_svg,
        encoding="utf-8",
    )

    print(f"Enhanced SVG written to: {args.svg_path}")


if __name__ == "__main__":
    main()
