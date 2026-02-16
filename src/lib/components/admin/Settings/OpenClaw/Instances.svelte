<script lang="ts">
  export let entries: any[] = [];
  export let loading = false;
  export let lastError: string | null = null;
  export let statusMessage: string | null = null;
  
  function formatLastInput(seconds: number | null): string {
    if (seconds === null) return 'n/a';
    if (seconds < 60) return `${seconds}s ago`;
    const minutes = Math.floor(seconds / 60);
    if (minutes < 60) return `${minutes}m ago`;
    const hours = Math.floor(minutes / 60);
    return `${hours}h ago`;
  }
  
  function getModeColor(mode: string): string {
    switch (mode) {
      case 'chat': return 'bg-blue-500';
      case 'admin': return 'bg-purple-500';
      case 'readonly': return 'bg-gray-500';
      default: return 'bg-gray-400';
    }
  }
</script>

<div class="instances-panel">
  <div class="flex items-center justify-between mb-6">
    <div>
      <h2 class="text-2xl font-bold">🔗 Connected Instances</h2>
      <p class="text-gray-500 dark:text-gray-400">Presence beacons from the gateway and clients.</p>
    </div>
    <button 
      class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition disabled:opacity-50"
      disabled={loading}
      on:click
    >
      {loading ? 'Loading...' : '🔄 Refresh'}
    </button>
  </div>
  
  {#if lastError}
    <div class="bg-red-50 dark:bg-red-900/20 border border-red-200 dark:border-red-800 rounded-lg p-4 mb-4">
      <p class="text-red-600 dark:text-red-400">{lastError}</p>
    </div>
  {/if}
  
  {#if statusMessage}
    <div class="bg-blue-50 dark:bg-blue-900/20 border border-blue-200 dark:border-blue-800 rounded-lg p-4 mb-4">
      <p class="text-blue-600 dark:text-blue-400">{statusMessage}</p>
    </div>
  {/if}
  
  <div class="bg-white dark:bg-gray-800 rounded-lg shadow overflow-hidden">
    {#if entries.length === 0}
      <div class="p-8 text-center text-gray-500">
        <p class="text-lg">No instances reported yet.</p>
      </div>
    {:else}
      <table class="w-full">
        <thead class="bg-gray-50 dark:bg-gray-900">
          <tr>
            <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">Instance</th>
            <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">Mode</th>
            <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">Roles</th>
            <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">Scopes</th>
            <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">Last Input</th>
            <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">Agent ID</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-200 dark:divide-gray-700">
          {#each entries as entry}
            <tr>
              <td class="px-4 py-3">
                <div class="font-medium">{entry.name || 'Unknown'}</div>
                <div class="text-xs text-gray-500">{entry.id || entry.agentId}</div>
              </td>
              <td class="px-4 py-3">
                <span class={`inline-flex items-center gap-1 text-xs px-2 py-0.5 rounded-full ${getModeColor(entry.mode)} text-white`}>
                  {entry.mode || 'unknown'}
                </span>
              </td>
              <td class="px-4 py-3">
                <div class="flex flex-wrap gap-1">
                  {#each (entry.roles || []).filter(Boolean) as role}
                    <span class="px-2 py-0.5 text-xs bg-gray-100 dark:bg-gray-700 rounded">{role}</span>
                  {/each}
                  {#if !entry.roles?.filter(Boolean).length}
                    <span class="text-gray-400 text-sm">—</span>
                  {/if}
                </div>
              </td>
              <td class="px-4 py-3">
                <div class="flex flex-wrap gap-1">
                  {#each (entry.scopes || []).filter(Boolean).slice(0, 3) as scope}
                    <span class="px-2 py-0.5 text-xs bg-purple-100 dark:bg-purple-900/30 text-purple-700 rounded">{scope}</span>
                  {/each}
                  {#if (entry.scopes?.filter(Boolean).length || 0) > 3}
                    <span class="text-xs text-gray-500">+{(entry.scopes?.filter(Boolean).length || 0) - 3} more</span>
                  {/if}
                </div>
              </td>
              <td class="px-4 py-3 text-sm text-gray-500">
                {formatLastInput(entry.lastInputSeconds)}
              </td>
              <td class="px-4 py-3 font-mono text-xs">
                {entry.agentId || '—'}
              </td>
            </tr>
          {/each}
        </tbody>
      </table>
    {/if}
  </div>
</div>

<style>
  .instances-panel {
    padding: 1rem;
  }
</style>
