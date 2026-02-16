<script lang="ts">
  export let agents: any[] = [];
  export let selectedAgent: string | null = null;
  export let loading = false;
  
  // Sub-panel state
  type SubPanel = 'overview' | 'files' | 'tools' | 'skills' | 'channels' | 'cron';
  let activeSubPanel: SubPanel = 'overview';
  
  // Sample data for sub-panels
  let agentFiles: any[] = [];
  let agentChannels: any[] = [];
  let agentCronJobs: any[] = [];
  let agentTools: any[] = [];
  let agentSkills: any[] = [];
  
  function getStatusColor(status: string) {
    switch (status) {
      case 'online': return 'bg-green-500';
      case 'offline': return 'bg-red-500';
      case 'busy': return 'bg-yellow-500';
      default: return 'bg-gray-400';
    }
  }
  
  function formatBytes(bytes: number): string {
    if (bytes === 0) return '0 B';
    const k = 1024;
    const sizes = ['B', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
  }
  
  $: selectedAgentData = agents.find(a => a.id === selectedAgent);
</script>

<div class="agents-panel">
  <div class="flex items-center justify-between mb-6">
    <h2 class="text-2xl font-bold">🤖 Agents</h2>
    <button class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition">
      + Add Agent
    </button>
  </div>
  
  <!-- Agent Selector -->
  {#if agents.length > 0}
    <div class="mb-4">
      <label class="block text-sm font-medium mb-2">Select Agent:</label>
      <select 
        bind:value={selectedAgent}
        class="w-full px-4 py-2 bg-white dark:bg-gray-800 border border-gray-300 dark:border-gray-600 rounded-lg"
      >
        {#each agents as agent}
          <option value={agent.id}>{agent.name} ({agent.status})</option>
        {/each}
      </select>
    </div>
  {/if}
  
  <!-- Sub-Panels Tabs -->
  <div class="flex gap-2 mb-4 border-b border-gray-200 dark:border-gray-700 pb-2 overflow-x-auto">
    <button 
      class="px-3 py-1.5 rounded-lg transition whitespace-nowrap {activeSubPanel === 'overview' ? 'bg-blue-100 dark:bg-blue-900/30 text-blue-700 dark:text-blue-300' : 'hover:bg-gray-100 dark:hover:bg-gray-800'}"
      on:click={() => activeSubPanel = 'overview'}
    >
      📊 Overview
    </button>
    <button 
      class="px-3 py-1.5 rounded-lg transition whitespace-nowrap {activeSubPanel === 'files' ? 'bg-blue-100 dark:bg-blue-900/30 text-blue-700 dark:text-blue-300' : 'hover:bg-gray-100 dark:hover:bg-gray-800'}"
      on:click={() => activeSubPanel = 'files'}
    >
      📁 Files
    </button>
    <button 
      class="px-3 py-1.5 rounded-lg transition whitespace-nowrap {activeSubPanel === 'tools' ? 'bg-blue-100 dark:bg-blue-900/30 text-blue-700 dark:text-blue-300' : 'hover:bg-gray-100 dark:hover:bg-gray-800'}"
      on:click={() => activeSubPanel = 'tools'}
    >
      🔧 Tools
    </button>
    <button 
      class="px-3 py-1.5 rounded-lg transition whitespace-nowrap {activeSubPanel === 'skills' ? 'bg-blue-100 dark:bg-blue-900/30 text-blue-700 dark:text-blue-300' : 'hover:bg-gray-100 dark:hover:bg-gray-800'}"
      on:click={() => activeSubPanel = 'skills'}
    >
      🧩 Skills
    </button>
    <button 
      class="px-3 py-1.5 rounded-lg transition whitespace-nowrap {activeSubPanel === 'channels' ? 'bg-blue-100 dark:bg-blue-900/30 text-blue-700 dark:text-blue-300' : 'hover:bg-gray-100 dark:hover:bg-gray-800'}"
      on:click={() => activeSubPanel = 'channels'}
    >
      📱 Channels
    </button>
    <button 
      class="px-3 py-1.5 rounded-lg transition whitespace-nowrap {activeSubPanel === 'cron' ? 'bg-blue-100 dark:bg-blue-900/30 text-blue-700 dark:text-blue-300' : 'hover:bg-gray-100 dark:hover:bg-gray-800'}"
      on:click={() => activeSubPanel = 'cron'}
    >
      ⏰ Cron
    </button>
  </div>
  
  {#if loading}
    <div class="flex items-center justify-center py-12">
      <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600"></div>
    </div>
  {:else if !selectedAgentData}
    <!-- Agent Grid (when no agent selected) -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      {#each agents as agent}
        <button 
          class="bg-white dark:bg-gray-800 rounded-lg p-4 shadow border-2 border-transparent hover:border-blue-500 transition text-left"
          on:click={() => selectedAgent = agent.id}
        >
          <div class="flex items-center gap-3 mb-3">
            <span class={`w-3 h-3 rounded-full ${getStatusColor(agent.status)}`}></span>
            <span class="font-semibold">{agent.name}</span>
          </div>
          <div class="text-sm text-gray-500 dark:text-gray-400">
            <p>Platform: {agent.platform || 'unknown'}</p>
            <p>Last seen: {agent.last_seen ? new Date(agent.last_seen).toLocaleString() : 'never'}</p>
          </div>
        </button>
      {/each}
      
      {#if agents.length === 0}
        <div class="col-span-full text-center py-12 text-gray-500">
          <p class="text-lg">No agents found</p>
          <p class="text-sm">Connect an agent to get started</p>
        </div>
      {/if}
    </div>
  {:else}
    <!-- Selected Agent Detail View -->
    {#if activeSubPanel === 'overview'}
      <div class="bg-white dark:bg-gray-800 rounded-lg p-6 shadow">
        <h3 class="text-xl font-semibold mb-4">Agent Context</h3>
        <div class="grid grid-cols-2 md:grid-cols-3 gap-4">
          <div>
            <div class="text-sm text-gray-500">Workspace</div>
            <div class="font-mono">{selectedAgentData.workspace || 'default'}</div>
          </div>
          <div>
            <div class="text-sm text-gray-500">Primary Model</div>
            <div class="font-mono">{selectedAgentData.model || 'N/A'}</div>
          </div>
          <div>
            <div class="text-sm text-gray-500">Status</div>
            <span class={`inline-flex items-center gap-1 text-xs px-2 py-0.5 rounded-full ${getStatusColor(selectedAgentData.status)} text-white`}>
              {selectedAgentData.status}
            </span>
          </div>
          <div>
            <div class="text-sm text-gray-500">Agent ID</div>
            <div class="font-mono text-xs">{selectedAgentData.id}</div>
          </div>
          <div>
            <div class="text-sm text-gray-500">Last Seen</div>
            <div>{selectedAgentData.last_seen ? new Date(selectedAgentData.last_seen).toLocaleString() : 'never'}</div>
          </div>
          <div>
            <div class="text-sm text-gray-500">Capabilities</div>
            <div class="flex flex-wrap gap-1 mt-1">
              {#each selectedAgentData.capabilities || [] as cap}
                <span class="px-2 py-0.5 text-xs bg-gray-100 dark:bg-gray-700 rounded">{cap}</span>
              {/each}
            </div>
          </div>
        </div>
        
        <div class="mt-6 flex gap-2">
          <button class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700">
            Configure
          </button>
          <button class="px-4 py-2 bg-gray-200 dark:bg-gray-700 rounded-lg hover:bg-gray-300 dark:hover:bg-gray-600">
            View Chat
          </button>
          <button 
            class="px-4 py-2 bg-gray-200 dark:bg-gray-700 rounded-lg hover:bg-gray-300"
            on:click={() => selectedAgent = null}
          >
            Back to List
          </button>
        </div>
      </div>
    
    {:else if activeSubPanel === 'files'}
      <div class="bg-white dark:bg-gray-800 rounded-lg p-6 shadow">
        <h3 class="text-xl font-semibold mb-4">📁 Agent Files</h3>
        <div class="text-gray-500 text-center py-8">
          <p>No files uploaded yet</p>
          <button class="mt-4 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700">
            Upload File
          </button>
        </div>
      </div>
    
    {:else if activeSubPanel === 'tools'}
      <div class="bg-white dark:bg-gray-800 rounded-lg p-6 shadow">
        <h3 class="text-xl font-semibold mb-4">🔧 Tools</h3>
        <div class="text-gray-500 text-center py-8">
          <p>No tools configured</p>
        </div>
      </div>
    
    {:else if activeSubPanel === 'skills'}
      <div class="bg-white dark:bg-gray-800 rounded-lg p-6 shadow">
        <h3 class="text-xl font-semibold mb-4">🧩 Skills</h3>
        <div class="text-gray-500 text-center py-8">
          <p>No skills enabled</p>
        </div>
      </div>
    
    {:else if activeSubPanel === 'channels'}
      <div class="bg-white dark:bg-gray-800 rounded-lg p-6 shadow">
        <h3 class="text-xl font-semibold mb-4">📱 Channels</h3>
        <div class="text-gray-500 text-center py-8">
          <p>No channels configured</p>
        </div>
      </div>
    
    {:else if activeSubPanel === 'cron'}
      <div class="bg-white dark:bg-gray-800 rounded-lg p-6 shadow">
        <h3 class="text-xl font-semibold mb-4">⏰ Cron Jobs</h3>
        <div class="text-gray-500 text-center py-8">
          <p>No cron jobs configured</p>
        </div>
      </div>
    {/if}
  {/if}
</div>

<style>
  .agents-panel {
    padding: 1rem;
  }
</style>
