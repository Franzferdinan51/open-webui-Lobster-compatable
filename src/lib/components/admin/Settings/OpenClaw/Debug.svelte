<script lang="ts">
  export let debugInfo: any = {
    gatewayVersion: 'unknown',
    openclawVersion: 'unknown',
    nodeVersion: 'unknown',
    platform: 'unknown',
    uptime: 'unknown',
    memory: 'unknown',
  };
  export let loading = false;
  
  function copyToClipboard(text: string) {
    navigator.clipboard.writeText(text);
  }
</script>

<div class="debug-panel">
  <div class="flex items-center justify-between mb-6">
    <div>
      <h2 class="text-2xl font-bold">🔧 Debug Info</h2>
      <p class="text-gray-500 dark:text-gray-400">System diagnostics and info</p>
    </div>
    <button 
      class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition"
      on:click
    >
      🔄 Refresh
    </button>
  </div>
  
  <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <!-- Gateway Info -->
    <div class="bg-white dark:bg-gray-800 rounded-lg p-4 shadow">
      <div class="flex items-center justify-between mb-3">
        <h3 class="font-semibold">🖥️ Gateway</h3>
        <button 
          class="text-xs px-2 py-1 bg-gray-100 dark:bg-gray-700 rounded hover:bg-gray-200"
          on:click={() => copyToClipboard(debugInfo.gatewayVersion)}
        >
          📋 Copy
        </button>
      </div>
      <div class="space-y-2 text-sm">
        <div class="flex justify-between">
          <span class="text-gray-500">Version:</span>
          <span class="font-mono">{debugInfo.gatewayVersion}</span>
        </div>
        <div class="flex justify-between">
          <span class="text-gray-500">Uptime:</span>
          <span>{debugInfo.uptime}</span>
        </div>
      </div>
    </div>
    
    <!-- OpenClaw Info -->
    <div class="bg-white dark:bg-gray-800 rounded-lg p-4 shadow">
      <div class="flex items-center justify-between mb-3">
        <h3 class="font-semibold">🦞 OpenClaw</h3>
        <button 
          class="text-xs px-2 py-1 bg-gray-100 dark:bg-gray-700 rounded hover:bg-gray-200"
          on:click={() => copyToClipboard(debugInfo.openclawVersion)}
        >
          📋 Copy
        </button>
      </div>
      <div class="space-y-2 text-sm">
        <div class="flex justify-between">
          <span class="text-gray-500">Version:</span>
          <span class="font-mono">{debugInfo.openclawVersion}</span>
        </div>
        <div class="flex justify-between">
          <span class="text-gray-500">Platform:</span>
          <span>{debugInfo.platform}</span>
        </div>
      </div>
    </div>
    
    <!-- Node Info -->
    <div class="bg-white dark:bg-gray-800 rounded-lg p-4 shadow">
      <div class="flex items-center justify-between mb-3">
        <h3 class="font-semibold">💻 Node</h3>
        <button 
          class="text-xs px-2 py-1 bg-gray-100 dark:bg-gray-700 rounded hover:bg-gray-200"
          on:click={() => copyToClipboard(debugInfo.nodeVersion)}
        >
          📋 Copy
        </button>
      </div>
      <div class="space-y-2 text-sm">
        <div class="flex justify-between">
          <span class="text-gray-500">Node.js:</span>
          <span class="font-mono">{debugInfo.nodeVersion}</span>
        </div>
        <div class="flex justify-between">
          <span class="text-gray-500">Memory:</span>
          <span>{debugInfo.memory}</span>
        </div>
      </div>
    </div>
    
    <!-- Network Info -->
    <div class="bg-white dark:bg-gray-800 rounded-lg p-4 shadow">
      <h3 class="font-semibold mb-3">🌐 Network</h3>
      <div class="space-y-2 text-sm">
        <div class="flex justify-between">
          <span class="text-gray-500">Gateway:</span>
          <span class="font-mono">100.106.80.61:18789</span>
        </div>
        <div class="flex justify-between">
          <span class="text-gray-500">WebUI:</span>
          <span class="font-mono">localhost:8080</span>
        </div>
        <div class="flex justify-between">
          <span class="text-gray-500">Agent Mesh:</span>
          <span class="font-mono">100.74.88.40:4000</span>
        </div>
      </div>
    </div>
  </div>
  
  <!-- Quick Actions -->
  <div class="mt-6">
    <h3 class="text-lg font-semibold mb-3">Quick Actions</h3>
    <div class="flex flex-wrap gap-2">
      <button class="px-4 py-2 bg-red-100 dark:bg-red-900/30 text-red-700 rounded-lg hover:bg-red-200">
        🗑️ Clear Cache
      </button>
      <button class="px-4 py-2 bg-yellow-100 dark:bg-yellow-900/30 text-yellow-700 rounded-lg hover:bg-yellow-200">
        📜 View Logs
      </button>
      <button class="px-4 py-2 bg-purple-100 dark:bg-purple-900/30 text-purple-700 rounded-lg hover:bg-purple-200">
        🔌 Restart Gateway
      </button>
      <button class="px-4 py-2 bg-blue-100 dark:bg-blue-900/30 text-blue-700 rounded-lg hover:bg-blue-200">
        📤 Export Config
      </button>
    </div>
  </div>
</div>

<style>
  .debug-panel {
    padding: 1rem;
  }
</style>
