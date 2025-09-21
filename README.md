<div align="center">

<!-- Animated Liquid Glass Header with Floating Particles -->
<div style="position: relative; background: linear-gradient(135deg, rgba(0,188,212,0.15) 0%, rgba(255,255,255,0.08) 25%, rgba(0,255,255,0.12) 50%, rgba(255,255,255,0.05) 75%, rgba(0,188,212,0.1) 100%); backdrop-filter: blur(25px); border-radius: 30px; padding: 40px; margin: 30px 0; box-shadow: 0 12px 40px rgba(31,38,135,0.4), inset 0 2px 0 rgba(255,255,255,0.3), inset 0 -2px 0 rgba(0,188,212,0.2); border: 2px solid rgba(255,255,255,0.25); overflow: hidden; animation: liquidPulse 4s ease-in-out infinite;">

<!-- Floating Electrolyte Particles -->
<div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; overflow: hidden;">
  <div style="position: absolute; top: 20%; left: 10%; width: 6px; height: 6px; background: radial-gradient(circle, rgba(0,255,255,0.9), transparent); border-radius: 50%; animation: float1 6s ease-in-out infinite, sparkle 2s linear infinite;"></div>
  <div style="position: absolute; top: 60%; left: 80%; width: 4px; height: 4px; background: radial-gradient(circle, rgba(255,255,255,0.8), transparent); border-radius: 50%; animation: float2 8s ease-in-out infinite, sparkle 1.5s linear infinite;"></div>
  <div style="position: absolute; top: 30%; left: 70%; width: 8px; height: 8px; background: radial-gradient(circle, rgba(0,188,212,0.9), transparent); border-radius: 50%; animation: float3 7s ease-in-out infinite, sparkle 2.5s linear infinite;"></div>
  <div style="position: absolute; top: 80%; left: 20%; width: 5px; height: 5px; background: radial-gradient(circle, rgba(255,255,255,0.7), transparent); border-radius: 50%; animation: float4 5s ease-in-out infinite, sparkle 1.8s linear infinite;"></div>
  <div style="position: absolute; top: 15%; left: 60%; width: 7px; height: 7px; background: radial-gradient(circle, rgba(0,255,255,0.8), transparent); border-radius: 50%; animation: float1 9s ease-in-out infinite, sparkle 2.2s linear infinite;"></div>
</div>

<!-- Reflection Layer -->
<div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(135deg, rgba(255,255,255,0.2) 0%, transparent 40%, rgba(0,255,255,0.1) 60%, rgba(255,255,255,0.15) 100%); border-radius: 30px; animation: reflectionShift 8s linear infinite;"></div>

<!-- Profile Image with Liquid Glass Effect -->
<div style="position: relative; display: inline-block; margin-bottom: 20px;">
  <img src="https://raw.githubusercontent.com/Lintshiwe/Lintshiwe/main/slade-logo.png"
       width="160"
       alt="Slade The Deceiver Logo"
       style="border-radius: 25px; background: rgba(255,255,255,0.2); backdrop-filter: blur(15px); box-shadow: 0 12px 40px rgba(0,255,255,0.3), inset 0 2px 0 rgba(255,255,255,0.4); border: 2px solid rgba(255,255,255,0.3); animation: imageGlow 3s ease-in-out infinite alternate;" />
  <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(45deg, rgba(255,255,255,0.3) 0%, transparent 30%, rgba(0,255,255,0.2) 70%, rgba(255,255,255,0.2) 100%); border-radius: 25px; animation: reflectionSweep 4s linear infinite;"></div>
</div>

<h1 style="color: #00bcd4; text-shadow: 0 0 20px rgba(0,188,212,0.6), 0 0 40px rgba(0,255,255,0.4); font-size: 2.5em; margin: 20px 0; animation: textGlow 3s ease-in-out infinite alternate;">
  Hey there, I'm Lintshiwe 👨🏾‍💻
</h1>

<p style="color: #ffffff; font-size: 1.3em; text-shadow: 0 2px 10px rgba(0,0,0,0.5); margin: 15px 0; background: rgba(255,255,255,0.1); backdrop-filter: blur(10px); border-radius: 15px; padding: 15px 25px; border: 1px solid rgba(255,255,255,0.2); animation: subtlePulse 5s ease-in-out infinite;">
  Code Stylist · UI/UX Explorer · Terminal Enthusiast · Offensive Security Learner
</p>

<p style="color: #e0e0e0; font-size: 1.1em; text-shadow: 0 2px 8px rgba(0,0,0,0.3); background: rgba(255,255,255,0.08); backdrop-filter: blur(8px); border-radius: 12px; padding: 12px 20px; border: 1px solid rgba(255,255,255,0.15); animation: subtlePulse 6s ease-in-out infinite;">
  Building full-stack experiences that blend performance, creativity, and secure tech.
</p>

<style>
@keyframes liquidPulse {
  0%, 100% { 
    box-shadow: 0 12px 40px rgba(31,38,135,0.4), inset 0 2px 0 rgba(255,255,255,0.3), inset 0 -2px 0 rgba(0,188,212,0.2);
    transform: translateY(0px);
  }
  50% { 
    box-shadow: 0 18px 60px rgba(31,38,135,0.6), inset 0 3px 0 rgba(255,255,255,0.4), inset 0 -3px 0 rgba(0,188,212,0.3);
    transform: translateY(-5px);
  }
}

@keyframes reflectionShift {
  0% { background: linear-gradient(135deg, rgba(255,255,255,0.2) 0%, transparent 40%, rgba(0,255,255,0.1) 60%, rgba(255,255,255,0.15) 100%); }
  25% { background: linear-gradient(225deg, rgba(0,255,255,0.15) 0%, transparent 30%, rgba(255,255,255,0.2) 70%, rgba(0,188,212,0.1) 100%); }
  50% { background: linear-gradient(315deg, rgba(255,255,255,0.25) 0%, transparent 35%, rgba(0,255,255,0.15) 65%, rgba(255,255,255,0.1) 100%); }
  75% { background: linear-gradient(45deg, rgba(0,188,212,0.2) 0%, transparent 40%, rgba(255,255,255,0.15) 60%, rgba(0,255,255,0.1) 100%); }
  100% { background: linear-gradient(135deg, rgba(255,255,255,0.2) 0%, transparent 40%, rgba(0,255,255,0.1) 60%, rgba(255,255,255,0.15) 100%); }
}

@keyframes float1 {
  0%, 100% { transform: translateY(0px) translateX(0px) scale(1); opacity: 0.7; }
  25% { transform: translateY(-20px) translateX(10px) scale(1.2); opacity: 1; }
  50% { transform: translateY(-40px) translateX(-15px) scale(0.8); opacity: 0.5; }
  75% { transform: translateY(-20px) translateX(5px) scale(1.1); opacity: 0.9; }
}

@keyframes float2 {
  0%, 100% { transform: translateY(0px) translateX(0px) scale(1); opacity: 0.8; }
  33% { transform: translateY(-30px) translateX(-20px) scale(1.3); opacity: 0.6; }
  66% { transform: translateY(-15px) translateX(25px) scale(0.9); opacity: 1; }
}

@keyframes float3 {
  0%, 100% { transform: translateY(0px) translateX(0px) scale(1); opacity: 0.6; }
  50% { transform: translateY(-35px) translateX(-10px) scale(1.4); opacity: 1; }
}

@keyframes float4 {
  0%, 100% { transform: translateY(0px) translateX(0px) scale(1); opacity: 0.9; }
  40% { transform: translateY(-25px) translateX(15px) scale(0.7); opacity: 0.4; }
  80% { transform: translateY(-45px) translateX(-5px) scale(1.2); opacity: 0.8; }
}

@keyframes sparkle {
  0%, 100% { box-shadow: 0 0 5px rgba(255,255,255,0.8), 0 0 10px rgba(0,255,255,0.6); }
  50% { box-shadow: 0 0 20px rgba(255,255,255,1), 0 0 30px rgba(0,255,255,0.9), 0 0 40px rgba(0,188,212,0.7); }
}

@keyframes imageGlow {
  0% { box-shadow: 0 12px 40px rgba(0,255,255,0.3), inset 0 2px 0 rgba(255,255,255,0.4); }
  100% { box-shadow: 0 18px 60px rgba(0,255,255,0.5), inset 0 3px 0 rgba(255,255,255,0.6); }
}

@keyframes textGlow {
  0% { text-shadow: 0 0 20px rgba(0,188,212,0.6), 0 0 40px rgba(0,255,255,0.4); }
  100% { text-shadow: 0 0 30px rgba(0,188,212,0.8), 0 0 60px rgba(0,255,255,0.6), 0 0 80px rgba(255,255,255,0.3); }
}

@keyframes reflectionSweep {
  0% { background: linear-gradient(45deg, rgba(255,255,255,0.3) 0%, transparent 30%, rgba(0,255,255,0.2) 70%, rgba(255,255,255,0.2) 100%); }
  25% { background: linear-gradient(135deg, transparent 0%, rgba(255,255,255,0.4) 40%, rgba(0,255,255,0.3) 60%, transparent 100%); }
  50% { background: linear-gradient(225deg, rgba(0,255,255,0.2) 0%, transparent 30%, rgba(255,255,255,0.3) 70%, rgba(0,188,212,0.2) 100%); }
  75% { background: linear-gradient(315deg, transparent 0%, rgba(0,255,255,0.3) 40%, rgba(255,255,255,0.4) 60%, transparent 100%); }
  100% { background: linear-gradient(45deg, rgba(255,255,255,0.3) 0%, transparent 30%, rgba(0,255,255,0.2) 70%, rgba(255,255,255,0.2) 100%); }
}

@keyframes subtlePulse {
  0%, 100% { transform: scale(1); box-shadow: 0 4px 20px rgba(0,0,0,0.2); }
  50% { transform: scale(1.02); box-shadow: 0 8px 40px rgba(0,255,255,0.3); }
}
</style>

</div>

---

<!-- Liquid Glass UI Concept Section -->
<div style="position: relative; background: rgba(255,255,255,0.12); backdrop-filter: blur(20px); border-radius: 25px; padding: 30px; margin: 25px 0; box-shadow: 0 8px 35px rgba(0,0,0,0.15), inset 0 2px 0 rgba(255,255,255,0.3); border: 2px solid rgba(255,255,255,0.25); overflow: hidden; animation: cardFloat 8s ease-in-out infinite;">

<!-- Background Electrolytes -->
<div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none;">
  <div style="position: absolute; top: 25%; left: 15%; width: 3px; height: 3px; background: radial-gradient(circle, rgba(0,255,255,0.8), transparent); border-radius: 50%; animation: miniFloat1 4s ease-in-out infinite, sparkle 1.5s linear infinite;"></div>
  <div style="position: absolute; top: 70%; left: 85%; width: 4px; height: 4px; background: radial-gradient(circle, rgba(255,255,255,0.9), transparent); border-radius: 50%; animation: miniFloat2 5s ease-in-out infinite, sparkle 2s linear infinite;"></div>
  <div style="position: absolute; top: 45%; left: 90%; width: 2px; height: 2px; background: radial-gradient(circle, rgba(0,188,212,0.7), transparent); border-radius: 50%; animation: miniFloat3 3s ease-in-out infinite, sparkle 1.8s linear infinite;"></div>
</div>

<h2 align="center" style="color: #00bcd4; text-shadow: 0 0 15px rgba(0,188,212,0.7); margin-bottom: 20px; animation: textGlow 4s ease-in-out infinite alternate;">✨ Liquid Glass UI Concept ✨</h2>

<div align="center" style="margin: 20px 0;">
  <div style="position: relative; display: inline-block;">
    <img src="https://raw.githubusercontent.com/Lintshiwe/Lintshiwe/main/slade-logo.png" width="140" style="border-radius: 20px; background: rgba(255,255,255,0.2); backdrop-filter: blur(12px); box-shadow: 0 8px 30px rgba(0,255,255,0.4); border: 2px solid rgba(255,255,255,0.3); animation: conceptImageFloat 6s ease-in-out infinite;" alt="Liquid Glass UI" />
    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(45deg, rgba(255,255,255,0.4) 0%, transparent 50%, rgba(0,255,255,0.3) 100%); border-radius: 20px; animation: conceptReflection 3s linear infinite;"></div>
  </div>
</div>

<p align="center" style="color: #00bcd4; font-size: 1.2em; background: rgba(255,255,255,0.15); border-radius: 15px; padding: 20px 30px; box-shadow: 0 6px 30px rgba(0,0,0,0.15); backdrop-filter: blur(8px); border: 1px solid rgba(255,255,255,0.2); text-shadow: 0 2px 10px rgba(0,0,0,0.3); animation: descriptionPulse 7s ease-in-out infinite;">
<strong style="animation: textShimmer 3s linear infinite;">Liquid Glass UI</strong> is a glassmorphism-inspired interface style, blending frosted backgrounds, vibrant highlights, and soft shadows for a modern, immersive look.<br>
<em style="color: #e0e0e0;">Perfect for dashboards, modals, and creative web apps.</em>
</p>

<style>
@keyframes cardFloat {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-8px); }
}

@keyframes miniFloat1 {
  0%, 100% { transform: translateY(0px) translateX(0px); opacity: 0.6; }
  50% { transform: translateY(-15px) translateX(8px); opacity: 1; }
}

@keyframes miniFloat2 {
  0%, 100% { transform: translateY(0px) translateX(0px); opacity: 0.8; }
  50% { transform: translateY(-20px) translateX(-12px); opacity: 0.4; }
}

@keyframes miniFloat3 {
  0%, 100% { transform: translateY(0px) translateX(0px); opacity: 0.7; }
  50% { transform: translateY(-10px) translateX(5px); opacity: 1; }
}

@keyframes conceptImageFloat {
  0%, 100% { transform: translateY(0px) rotate(0deg); }
  25% { transform: translateY(-5px) rotate(1deg); }
  50% { transform: translateY(-8px) rotate(0deg); }
  75% { transform: translateY(-3px) rotate(-1deg); }
}

@keyframes conceptReflection {
  0% { background: linear-gradient(45deg, rgba(255,255,255,0.4) 0%, transparent 50%, rgba(0,255,255,0.3) 100%); }
  33% { background: linear-gradient(135deg, rgba(0,255,255,0.3) 0%, transparent 50%, rgba(255,255,255,0.4) 100%); }
  66% { background: linear-gradient(225deg, rgba(255,255,255,0.4) 0%, transparent 50%, rgba(0,255,255,0.3) 100%); }
  100% { background: linear-gradient(45deg, rgba(255,255,255,0.4) 0%, transparent 50%, rgba(0,255,255,0.3) 100%); }
}

@keyframes descriptionPulse {
  0%, 100% { box-shadow: 0 6px 30px rgba(0,0,0,0.15); transform: scale(1); }
  50% { box-shadow: 0 12px 50px rgba(0,255,255,0.25); transform: scale(1.01); }
}

@keyframes textShimmer {
  0% { color: #00bcd4; }
  50% { color: #00ffff; }
  100% { color: #00bcd4; }
}
</style>

</div>

---

<!-- About Me Section with Enhanced Liquid Glass -->
<div style="position: relative; background: rgba(255,255,255,0.1); backdrop-filter: blur(18px); border-radius: 20px; padding: 25px; margin: 20px 0; box-shadow: 0 6px 25px rgba(0,0,0,0.12), inset 0 1px 0 rgba(255,255,255,0.3); border: 1px solid rgba(255,255,255,0.2); overflow: hidden; animation: sectionWave 10s ease-in-out infinite;">

<!-- Section Electrolytes -->
<div style="position: absolute; top: 10%; right: 10%; width: 5px; height: 5px; background: radial-gradient(circle, rgba(0,255,255,0.9), transparent); border-radius: 50%; animation: sectionFloat1 7s ease-in-out infinite, sparkle 2.3s linear infinite;"></div>
<div style="position: absolute; bottom: 20%; left: 8%; width: 6px; height: 6px; background: radial-gradient(circle, rgba(255,255,255,0.8), transparent); border-radius: 50%; animation: sectionFloat2 9s ease-in-out infinite, sparkle 1.7s linear infinite;"></div>

<h2 style="color: #00bcd4; text-shadow: 0 0 12px rgba(0,188,212,0.6); margin-bottom: 20px; animation: headerGlow 5s ease-in-out infinite alternate;">🧠 About Me</h2>

<div style="color: #e0e0e0; line-height: 1.8; text-shadow: 0 1px 5px rgba(0,0,0,0.3);">

- 💡 Passionate about intuitive UI/UX, responsive design, and real-time web functionality
- 🧊 Designing with glassmorphism and Liquid Glass UI for next-gen web experiences
- 🔒 Exploring local-first security, password encryption, and browser data integration
- 💻 Devoted to scalable platforms with modular architecture (`Salon`)
- 🧑🏾‍🏫 Creating tech-driven learning spaces like `CourseCampus` for digital skill empowerment
- 🐧 Always curious — currently experimenting with Linux terminal interfaces in the browser
- ⚙️ Practicing DevOps automation with CI/CD pipelines, containerization, and infrastructure as code
- 🧵 Skilled in Red Hat System Administration — user management, SELinux, systemd, and secure networking

</div>

<style>
@keyframes sectionWave {
  0%, 100% { 
    background: rgba(255,255,255,0.1); 
    border-color: rgba(255,255,255,0.2);
  }
  50% { 
    background: rgba(255,255,255,0.15); 
    border-color: rgba(0,255,255,0.3);
  }
}

@keyframes sectionFloat1 {
  0%, 100% { transform: translateY(0px) translateX(0px) scale(1); }
  50% { transform: translateY(-25px) translateX(-15px) scale(1.5); }
}

@keyframes sectionFloat2 {
  0%, 100% { transform: translateY(0px) translateX(0px) scale(1); }
  50% { transform: translateY(-30px) translateX(20px) scale(1.2); }
}

@keyframes headerGlow {
  0% { text-shadow: 0 0 12px rgba(0,188,212,0.6); }
  100% { text-shadow: 0 0 20px rgba(0,188,212,0.8), 0 0 30px rgba(0,255,255,0.5); }
}
</style>

</div>

---

<!-- Tech Toolbox with Animated Icons -->
<div style="position: relative; background: rgba(255,255,255,0.12); backdrop-filter: blur(20px); border-radius: 25px; padding: 30px; margin: 25px 0; box-shadow: 0 8px 35px rgba(0,0,0,0.15), inset 0 2px 0 rgba(255,255,255,0.3); border: 2px solid rgba(255,255,255,0.25); overflow: hidden; animation: techPulse 8s ease-in-out infinite;">

<h2 style="color: #00bcd4; text-shadow: 0 0 15px rgba(0,188,212,0.7); text-align: center; margin-bottom: 25px; animation: techHeaderGlow 4s ease-in-out infinite alternate;">🔧 Tech Toolbox</h2>

<div align="center" style="animation: iconsFloat 6s ease-in-out infinite;">
  <img src="https://skillicons.dev/icons?i=ts,js,py,java,react,nextjs,nodejs,firebase,sqlite,tailwind,css,html,linux,git,github,vscode,docker,bash,ansible" alt="Tech Stack Icons" style="filter: drop-shadow(0 4px 15px rgba(0,255,255,0.3)); animation: iconsGlow 3s ease-in-out infinite alternate;" />
</div>

<style>
@keyframes techPulse {
  0%, 100% { 
    box-shadow: 0 8px 35px rgba(0,0,0,0.15), inset 0 2px 0 rgba(255,255,255,0.3);
    transform: scale(1);
  }
  50% { 
    box-shadow: 0 12px 50px rgba(0,255,255,0.2), inset 0 3px 0 rgba(255,255,255,0.4);
    transform: scale(1.01);
  }
}

@keyframes techHeaderGlow {
  0% { text-shadow: 0 0 15px rgba(0,188,212,0.7); }
  100% { text-shadow: 0 0 25px rgba(0,188,212,0.9), 0 0 35px rgba(0,255,255,0.6); }
}

@keyframes iconsFloat {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-8px); }
}

@keyframes iconsGlow {
  0% { filter: drop-shadow(0 4px 15px rgba(0,255,255,0.3)); }
  100% { filter: drop-shadow(0 6px 25px rgba(0,255,255,0.5)) drop-shadow(0 0 15px rgba(255,255,255,0.3)); }
}
</style>

</div>

---

<!-- GitHub Stats with Liquid Glass Enhancement -->
<div style="position: relative; background: rgba(255,255,255,0.1); backdrop-filter: blur(18px); border-radius: 20px; padding: 25px; margin: 20px 0; box-shadow: 0 6px 30px rgba(0,0,0,0.12), inset 0 1px 0 rgba(255,255,255,0.25); border: 1px solid rgba(255,255,255,0.2); overflow: hidden; animation: statsFloat 9s ease-in-out infinite;">

<!-- Stats Electrolytes -->
<div style="position: absolute; top: 15%; left: 5%; width: 4px; height: 4px; background: radial-gradient(circle, rgba(0,255,255,0.8), transparent); border-radius: 50%; animation: statsFloat1 6s ease-in-out infinite, sparkle 2.1s linear infinite;"></div>
<div style="position: absolute; top: 80%; right: 10%; width: 5px; height: 5px; background: radial-gradient(circle, rgba(255,255,255,0.9), transparent); border-radius: 50%; animation: statsFloat2 8s ease-in-out infinite, sparkle 1.9s linear infinite;"></div>

<h2 style="color: #00bcd4; text-shadow: 0 0 12px rgba(0,188,212,0.6); text-align: center; margin-bottom: 25px; animation: statsHeaderPulse 5s ease-in-out infinite alternate;">📊 GitHub Stats</h2>

<div align="center" style="animation: statsImageFloat 7s ease-in-out infinite;">
  <img src="https://github-readme-stats.vercel.app/api?username=Lintshiwe&show_icons=true&theme=radical&hide_border=true&bg_color=00000000" alt="GitHub Stats" style="margin: 10px; border-radius: 15px; box-shadow: 0 8px 25px rgba(0,255,255,0.2); animation: statCardGlow 4s ease-in-out infinite alternate;" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Lintshiwe&layout=compact&theme=radical&hide_border=true&bg_color=00000000" alt="Top Languages" style="margin: 10px; border-radius: 15px; box-shadow: 0 8px 25px rgba(0,255,255,0.2); animation: statCardGlow 4s ease-in-out infinite alternate 0.5s;" />
</div>

<style>
@keyframes statsFloat {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-6px); }
}

@keyframes statsFloat1 {
  0%, 100% { transform: translateY(0px) translateX(0px) scale(1); opacity: 0.7; }
  50% { transform: translateY(-20px) translateX(15px) scale(1.3); opacity: 1; }
}

@keyframes statsFloat2 {
  0%, 100% { transform: translateY(0px) translateX(0px) scale(1); opacity: 0.8; }
  50% { transform: translateY(-25px) translateX(-10px) scale(1.4); opacity: 0.5; }
}

@keyframes statsHeaderPulse {
  0% { text-shadow: 0 0 12px rgba(0,188,212,0.6); }
  100% { text-shadow: 0 0 18px rgba(0,188,212,0.8), 0 0 25px rgba(0,255,255,0.5); }
}

@keyframes statsImageFloat {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-5px); }
}

@keyframes statCardGlow {
  0% { box-shadow: 0 8px 25px rgba(0,255,255,0.2); }
  100% { box-shadow: 0 12px 40px rgba(0,255,255,0.4), 0 0 20px rgba(255,255,255,0.2); }
}
</style>

</div>

---

<!-- Liquid Glass UI Code Example -->
<div style="position: relative; background: rgba(255,255,255,0.12); backdrop-filter: blur(20px); border-radius: 25px; padding: 30px; margin: 25px 0; box-shadow: 0 8px 35px rgba(0,0,0,0.15), inset 0 2px 0 rgba(255,255,255,0.3); border: 2px solid rgba(255,255,255,0.25); overflow: hidden; animation: codeWave 10s ease-in-out infinite;">

<!-- Code Section Electrolytes -->
<div style="position: absolute; top: 20%; right: 15%; width: 3px; height: 3px; background: radial-gradient(circle, rgba(0,255,255,0.9), transparent); border-radius: 50%; animation: codeFloat1 5s ease-in-out infinite, sparkle 2s linear infinite;"></div>
<div style="position: absolute; bottom: 25%; left: 12%; width: 4px; height: 4px; background: radial-gradient(circle, rgba(255,255,255,0.8), transparent); border-radius: 50%; animation: codeFloat2 7s ease-in-out infinite, sparkle 1.6s linear infinite;"></div>

<h2 style="color: #00bcd4; text-shadow: 0 0 15px rgba(0,188,212,0.7); text-align: center; margin-bottom: 25px; animation: codeHeaderShimmer 6s ease-in-out infinite alternate;">🪟 Liquid Glass UI Example</h2>

<div style="background: rgba(0,0,0,0.3); backdrop-filter: blur(10px); border-radius: 15px; padding: 20px; border: 1px solid rgba(255,255,255,0.1); box-shadow: inset 0 2px 10px rgba(0,0,0,0.5); animation: codeBlockPulse 8s ease-in-out infinite;">

```jsx
// React + Tailwind CSS Glassmorphism Card
<div className="bg-white/20 backdrop-blur-lg rounded-xl border border-white/30 shadow-lg p-6">
  <h3 className="text-cyan-400 font-bold text-lg mb-2">Liquid Glass UI Card</h3>
  <p className="text-white/80">
    A frosted glass effect for modern dashboards and modals.
  </p>
</div>
```

</div>

<style>
@keyframes codeWave {
  0%, 100% { 
    background: rgba(255,255,255,0.12);
    border-color: rgba(255,255,255,0.25);
  }
  50% { 
    background: rgba(255,255,255,0.18);
    border-color: rgba(0,255,255,0.4);
  }
}

@keyframes codeFloat1 {
  0%, 100% { transform: translateY(0px) translateX(0px) scale(1); opacity: 0.8; }
  50% { transform: translateY(-15px) translateX(-8px) scale(1.2); opacity: 1; }
}

@keyframes codeFloat2 {
  0%, 100% { transform: translateY(0px) translateX(0px) scale(1); opacity: 0.6; }
  50% { transform: translateY(-18px) translateX(12px) scale(1.3); opacity: 0.9; }
}

@keyframes codeHeaderShimmer {
  0% { 
    text-shadow: 0 0 15px rgba(0,188,212,0.7);
    color: #00bcd4;
  }
  100% { 
    text-shadow: 0 0 25px rgba(0,188,212,0.9), 0 0 35px rgba(0,255,255,0.6);
    color: #00ffff;
  }
}

@keyframes codeBlockPulse {
  0%, 100% { 
    box-shadow: inset 0 2px 10px rgba(0,0,0,0.5);
    transform: scale(1);
  }
  50% { 
    box-shadow: inset 0 4px 20px rgba(0,0,0,0.7), 0 0 15px rgba(0,255,255,0.2);
    transform: scale(1.005);
  }
}
</style>

</div>

---

<!-- Featured Projects Section with Enhanced Animation -->
<div style="position: relative; background: rgba(255,255,255,0.1); backdrop-filter: blur(18px); border-radius: 20px; padding: 25px; margin: 20px 0; box-shadow: 0 6px 30px rgba(0,0,0,0.12), inset 0 1px 0 rgba(255,255,255,0.25); border: 1px solid rgba(255,255,255,0.2); overflow: hidden; animation: projectsFloat 11s ease-in-out infinite;">

<!-- Projects Electrolytes -->
<div style="position: absolute; top: 12%; left: 8%; width: 6px; height: 6px; background: radial-gradient(circle, rgba(0,255,255,0.9), transparent); border-radius: 50%; animation: projectFloat1 8s ease-in-out infinite, sparkle 2.4s linear infinite;"></div>
<div style="position: absolute; top: 75%; right: 6%; width: 5px; height: 5px; background: radial-gradient(circle, rgba(255,255,255,0.8), transparent); border-radius: 50%; animation: projectFloat2 6s ease-in-out infinite, sparkle 1.8s linear infinite;"></div>
<div style="position: absolute; top: 45%; right: 20%; width: 4px; height: 4px; background: radial-gradient(circle, rgba(0,188,212,0.7), transparent); border-radius: 50%; animation: projectFloat3 9s ease-in-out infinite, sparkle 2.2s linear infinite;"></div>

<h2 style="color: #00bcd4; text-shadow: 0 0 12px rgba(0,188,212,0.6); text-align: center; margin-bottom: 25px; animation: projectHeaderPulse 5s ease-in-out infinite alternate;">🚀 Featured Projects</h2>

<div style="overflow-x: auto; animation: tableSlide 7s ease-in-out infinite;">

| 🌟 Project                                                                      | ⚡ Description                                           | 🛠️ Tech Stack                      |
| ------------------------------------------------------------------------------- | -------------------------------------------------------- | ---------------------------------- |
| [PasswordManager](https://github.com/Lintshiwe/PasswordManager)                 | Local-first encrypted vault with smart browser detection | Python · Tkinter · Fernet · SQLite |
| [CourseCampus](https://github.com/Lintshiwe/CourseCampus)                       | Web + terminal hybrid platform for student learning      | Next.js 14 · Tailwind · Firebase   |
| [Salon](https://github.com/Lintshiwe/Salon)                                     | Reusable UI + scalable frontend boilerplate              | React · TypeScript · Tailwind CSS  |
| [JunksElectricalSolution](https://github.com/Lintshiwe/JunksElectricalSolution) | Real-time quote system for electrical services           | Next.js · Firebase · Tailwind      |
| [Slade_MITM](https://github.com/Lintshiwe/Slade_MITM)                           | MITM proxy for ethical cybersecurity training            | Python · mitmproxy                 |

</div>

<style>
@keyframes projectsFloat {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-7px); }
}

@keyframes projectFloat1 {
  0%, 100% { transform: translateY(0px) translateX(0px) scale(1); opacity: 0.8; }
  33% { transform: translateY(-20px) translateX(10px) scale(1.4); opacity: 1; }
  66% { transform: translateY(-35px) translateX(-5px) scale(0.9); opacity: 0.6; }
}

@keyframes projectFloat2 {
  0%, 100% { transform: translateY(0px) translateX(0px) scale(1); opacity: 0.7; }
  50% { transform: translateY(-25px) translateX(-15px) scale(1.3); opacity: 1; }
}

@keyframes projectFloat3 {
  0%, 100% { transform: translateY(0px) translateX(0px) scale(1); opacity: 0.9; }
  40% { transform: translateY(-18px) translateX(8px) scale(1.1); opacity: 0.5; }
  80% { transform: translateY(-30px) translateX(-12px) scale(1.2); opacity: 0.8; }
}

@keyframes projectHeaderPulse {
  0% { text-shadow: 0 0 12px rgba(0,188,212,0.6); }
  100% { text-shadow: 0 0 20px rgba(0,188,212,0.8), 0 0 30px rgba(0,255,255,0.5); }
}

@keyframes tableSlide {
  0%, 100% { transform: translateX(0px); }
  50% { transform: translateX(-2px); }
}
</style>

</div>

---

<!-- Currently Working On Section -->
<div style="position: relative; background: rgba(255,255,255,0.12); backdrop-filter: blur(20px); border-radius: 25px; padding: 30px; margin: 25px 0; box-shadow: 0 8px 35px rgba(0,0,0,0.15), inset 0 2px 0 rgba(255,255,255,0.3); border: 2px solid rgba(255,255,255,0.25); overflow: hidden; animation: workingPulse 9s ease-in-out infinite;">

<!-- Working Section Electrolytes -->
<div style="position: absolute; top: 18%; left: 12%; width: 5px; height: 5px; background: radial-gradient(circle, rgba(0,255,255,0.9), transparent); border-radius: 50%; animation: workingFloat1 6s ease-in-out infinite, sparkle 2.1s linear infinite;"></div>
<div style="position: absolute; bottom: 30%; right: 8%; width: 4px; height: 4px; background: radial-gradient(circle, rgba(255,255,255,0.8), transparent); border-radius: 50%; animation: workingFloat2 8s ease-in-out infinite, sparkle 1.7s linear infinite;"></div>

<h2 style="color: #00bcd4; text-shadow: 0 0 15px rgba(0,188,212,0.7); text-align: center; margin-bottom: 25px; animation: workingHeaderGlow 4s ease-in-out infinite alternate;">🧪 Currently Working On</h2>

<div style="color: #e0e0e0; line-height: 1.8; text-shadow: 0 1px 5px rgba(0,0,0,0.3); animation: workingContentFloat 10s ease-in-out infinite;">

- 🎓 Linux-style browser terminals for education
- 🧊 Advancing Liquid Glass UI implementations in React and Tailwind
- 🔐 Enhancing local-first security patterns for web apps
- 🏗️ Building modular architectures for scalable platforms
- 🐧 Experimenting with browser-based terminal emulators

</div>

<style>
@keyframes workingPulse {
  0%, 100% { 
    box-shadow: 0 8px 35px rgba(0,0,0,0.15), inset 0 2px 0 rgba(255,255,255,0.3);
    transform: scale(1);
  }
  50% { 
    box-shadow: 0 12px 50px rgba(0,255,255,0.2), inset 0 3px 0 rgba(255,255,255,0.4);
    transform: scale(1.008);
  }
}

@keyframes workingFloat1 {
  0%, 100% { transform: translateY(0px) translateX(0px) scale(1); opacity: 0.8; }
  50% { transform: translateY(-22px) translateX(10px) scale(1.3); opacity: 1; }
}

@keyframes workingFloat2 {
  0%, 100% { transform: translateY(0px) translateX(0px) scale(1); opacity: 0.7; }
  50% { transform: translateY(-28px) translateX(-8px) scale(1.4); opacity: 0.9; }
}

@keyframes workingHeaderGlow {
  0% { text-shadow: 0 0 15px rgba(0,188,212,0.7); }
  100% { text-shadow: 0 0 25px rgba(0,188,212,0.9), 0 0 35px rgba(0,255,255,0.6); }
}

@keyframes workingContentFloat {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-3px); }
}
</style>

</div>

---

<!-- Quote Section -->
<div style="position: relative; background: rgba(255,255,255,0.08); backdrop-filter: blur(15px); border-radius: 18px; padding: 20px; margin: 18px 0; box-shadow: 0 4px 25px rgba(0,0,0,0.1), inset 0 1px 0 rgba(255,255,255,0.2); border: 1px solid rgba(255,255,255,0.15); overflow: hidden; animation: quoteFloat 12s ease-in-out infinite;">

<!-- Quote Electrolytes -->
<div style="position: absolute; top: 50%; left: 5%; width: 3px; height: 3px; background: radial-gradient(circle, rgba(0,255,255,0.8), transparent); border-radius: 50%; animation: quoteFloat1 7s ease-in-out infinite, sparkle 2s linear infinite;"></div>
<div style="position: absolute; top: 30%; right: 8%; width: 4px; height: 4px; background: radial-gradient(circle, rgba(255,255,255,0.9), transparent); border-radius: 50%; animation: quoteFloat2 5s ease-in-out infinite, sparkle 1.5s linear infinite;"></div>

<p align="center" style="color: #00bcd4; font-style: italic; font-size: 1.2em; text-shadow: 0 2px 10px rgba(0,188,212,0.4); animation: quotePulse 6s ease-in-out infinite alternate;">
  Minimal branding. Ethical code. Purpose-built tech.
</p>

<style>
@keyframes quoteFloat {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-5px); }
}

@keyframes quoteFloat1 {
  0%, 100% { transform: translateY(0px) translateX(0px) scale(1); opacity: 0.7; }
  50% { transform: translateY(-15px) translateX(8px) scale(1.2); opacity: 1; }
}

@keyframes quoteFloat2 {
  0%, 100% { transform: translateY(0px) translateX(0px) scale(1); opacity: 0.8; }
  50% { transform: translateY(-12px) translateX(-6px) scale(1.1); opacity: 0.6; }
}

@keyframes quotePulse {
  0% { 
    text-shadow: 0 2px 10px rgba(0,188,212,0.4);
    color: #00bcd4;
  }
  100% { 
    text-shadow: 0 4px 20px rgba(0,188,212,0.6), 0 0 15px rgba(0,255,255,0.4);
    color: #00ffff;
  }
}
</style>

</div>

---

<!-- Achievements Section -->
<div style="position: relative; background: rgba(255,255,255,0.12); backdrop-filter: blur(20px); border-radius: 25px; padding: 30px; margin: 25px 0; box-shadow: 0 8px 35px rgba(0,0,0,0.15), inset 0 2px 0 rgba(255,255,255,0.3); border: 2px solid rgba(255,255,255,0.25); overflow: hidden; animation: achievementWave 10s ease-in-out infinite;">

<!-- Achievement Electrolytes -->
<div style="position: absolute; top: 25%; right: 12%; width: 6px; height: 6px; background: radial-gradient(circle, rgba(0,255,255,0.9), transparent); border-radius: 50%; animation: achievementFloat1 8s ease-in-out infinite, sparkle 2.3s linear infinite;"></div>
<div style="position: absolute; bottom: 20%; left: 10%; width: 5px; height: 5px; background: radial-gradient(circle, rgba(255,255,255,0.8), transparent); border-radius: 50%; animation: achievementFloat2 6s ease-in-out infinite, sparkle 1.9s linear infinite;"></div>
<div style="position: absolute; top: 60%; left: 85%; width: 4px; height: 4px; background: radial-gradient(circle, rgba(0,188,212,0.7), transparent); border-radius: 50%; animation: achievementFloat3 9s ease-in-out infinite, sparkle 2.1s linear infinite;"></div>

<h2 style="color: #00bcd4; text-shadow: 0 0 15px rgba(0,188,212,0.7); text-align: center; margin-bottom: 25px; animation: achievementHeaderShimmer 5s ease-in-out infinite alternate;">🎯 Achievements & Fun Facts</h2>

<div style="color: #e0e0e0; line-height: 1.8; text-shadow: 0 1px 5px rgba(0,0,0,0.3); animation: achievementContentPulse 8s ease-in-out infinite;">

- 🏆 Built 5+ full-stack projects with modern web technologies
- 🌟 Passionate about open-source contributions and community learning
- 💡 Innovating UI/UX with glassmorphism and futuristic designs
- 🔧 Skilled in DevOps, containerization, and secure system administration
- 📚 Always learning — from browser terminals to ethical hacking

</div>

<style>
@keyframes achievementWave {
  0%, 100% { 
    background: rgba(255,255,255,0.12);
    border-color: rgba(255,255,255,0.25);
  }
  50% { 
    background: rgba(255,255,255,0.18);
    border-color: rgba(0,255,255,0.4);
  }
}

@keyframes achievementFloat1 {
  0%, 100% { transform: translateY(0px) translateX(0px) scale(1); opacity: 0.8; }
  33% { transform: translateY(-25px) translateX(-10px) scale(1.4); opacity: 1; }
  66% { transform: translateY(-15px) translateX(15px) scale(0.9); opacity: 0.6; }
}

@keyframes achievementFloat2 {
  0%, 100% { transform: translateY(0px) translateX(0px) scale(1); opacity: 0.7; }
  50% { transform: translateY(-30px) translateX(8px) scale(1.3); opacity: 1; }
}

@keyframes achievementFloat3 {
  0%, 100% { transform: translateY(0px) translateX(0px) scale(1); opacity: 0.9; }
  40% { transform: translateY(-20px) translateX(-12px) scale(1.1); opacity: 0.5; }
  80% { transform: translateY(-35px) translateX(5px) scale(1.2); opacity: 0.8; }
}

@keyframes achievementHeaderShimmer {
  0% { 
    text-shadow: 0 0 15px rgba(0,188,212,0.7);
    color: #00bcd4;
  }
  100% { 
    text-shadow: 0 0 25px rgba(0,188,212,0.9), 0 0 35px rgba(0,255,255,0.6);
    color: #00ffff;
  }
}

@keyframes achievementContentPulse {
  0%, 100% { transform: translateY(0px); opacity: 0.9; }
  50% { transform: translateY(-2px); opacity: 1; }
}
</style>

</div>

---

<!-- Connect Section with Enhanced Liquid Glass -->
<div style="position: relative; background: rgba(255,255,255,0.1); backdrop-filter: blur(18px); border-radius: 20px; padding: 25px; margin: 20px 0; box-shadow: 0 6px 30px rgba(0,0,0,0.12), inset 0 1px 0 rgba(255,255,255,0.25); border: 1px solid rgba(255,255,255,0.2); overflow: hidden; animation: connectFloat 11s ease-in-out infinite;">

<!-- Connect Electrolytes -->
<div style="position: absolute; top: 35%; left: 15%; width: 5px; height: 5px; background: radial-gradient(circle, rgba(0,255,255,0.9), transparent); border-radius: 50%; animation: connectFloat1 7s ease-in-out infinite, sparkle 2.2s linear infinite;"></div>
<div style="position: absolute; bottom: 40%; right: 12%; width: 6px; height: 6px; background: radial-gradient(circle, rgba(255,255,255,0.8), transparent); border-radius: 50%; animation: connectFloat2 9s ease-in-out infinite, sparkle 1.8s linear infinite;"></div>

<h2 style="color: #00bcd4; text-shadow: 0 0 12px rgba(0,188,212,0.6); text-align: center; margin-bottom: 25px; animation: connectHeaderGlow 4s ease-in-out infinite alternate;">🌐 Connect with Me</h2>

<div align="center" style="animation: socialIconsFloat 6s ease-in-out infinite;">
  <a href="https://github.com/Lintshiwe" target="_blank" style="display: inline-block; margin: 0 15px; animation: iconBounce 3s ease-in-out infinite;">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" width="40" alt="GitHub" style="filter: drop-shadow(0 4px 15px rgba(255,255,255,0.3)); transition: all 0.3s ease;" />
  </a>
  <a href="https://twitter.com/YourHandle" target="_blank" style="display: inline-block; margin: 0 15px; animation: iconBounce 3s ease-in-out infinite 0.5s;">
    <img src="https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/x.svg" width="40" alt="Twitter" style="filter: drop-shadow(0 4px 15px rgba(0,255,255,0.3)); transition: all 0.3s ease;" />
  </a>
  <a href="https://linkedin.com/in/YourProfile" target="_blank" style="display: inline-block; margin: 0 15px; animation: iconBounce 3s ease-in-out infinite 1s;">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" width="40" alt="LinkedIn" style="filter: drop-shadow(0 4px 15px rgba(0,120,215,0.3)); transition: all 0.3s ease;" />
  </a>
  <a href="mailto:your@email.com" style="display: inline-block; margin: 0 15px; animation: iconBounce 3s ease-in-out infinite 1.5s;">
    <img src="https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white" height="32" alt="Email" style="border-radius: 8px; filter: drop-shadow(0 4px 15px rgba(209,72,54,0.3)); transition: all 0.3s ease;" />
  </a>
</div>

<style>
@keyframes connectFloat {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-6px); }
}

@keyframes connectFloat1 {
  0%, 100% { transform: translateY(0px) translateX(0px) scale(1); opacity: 0.8; }
  50% { transform: translateY(-20px) translateX(12px) scale(1.3); opacity: 1; }
}

@keyframes connectFloat2 {
  0%, 100% { transform: translateY(0px) translateX(0px) scale(1); opacity: 0.7; }
  50% { transform: translateY(-25px) translateX(-8px) scale(1.4); opacity: 0.9; }
}

@keyframes connectHeaderGlow {
  0% { text-shadow: 0 0 12px rgba(0,188,212,0.6); }
  100% { text-shadow: 0 0 20px rgba(0,188,212,0.8), 0 0 30px rgba(0,255,255,0.5); }
}

@keyframes socialIconsFloat {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-4px); }
}

@keyframes iconBounce {
  0%, 100% { transform: translateY(0px) scale(1); }
  50% { transform: translateY(-8px) scale(1.1); }
}
</style>

</div>

</div>
