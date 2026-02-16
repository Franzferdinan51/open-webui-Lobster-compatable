<script lang="ts">
  export let approvals: any[] = [];
  export let loading = false;
  
  function formatRemaining(expiresAtMs: number): string {
    const remaining = Math.max(0, expiresAtMs - Date.now());
    if (remaining <= 0) return 'expired';
    const totalSeconds = Math.floor(remaining / 1000);
    if (totalSeconds < 60) return `${totalSeconds}s remaining`;
    const minutes = Math.floor(totalSeconds / 60);
    if (minutes < 60) return `${minutes}m remaining`;
    const hours = Math.floor(minutes / 60);
    return `${hours}h remaining`;
  }
  
  function getStatusColor(approved: boolean | null): string {
    if (approved === true) return 'bg-green-500';
    if (approved === false) return 'bg-red-500';
    return 'bg-yellow-500';
  }
</script>

<div class="exec-approval-panel">
  <div class="flex items-center justify-between mb-6">
    <div>
      <h2 class="text-2xl font-bold">⚠️ Exec Approvals</h2>
      <p class="text-gray-500 dark:text-gray-400">Pending command execution approvals</p>
    </div>
    <button 
      class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition"
      on:click
    >
      🔄 Refresh
    </button>
  </div>
  
  {#if loading}
    <div class="flex items-center justify-center py-12">
      <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600"></div>
    </div>
  {:else if approvals.length === 0}
    <div class="bg-green-50 dark:bg-green-900/20 border border-green-200 dark:border-green-800 rounded-lg p-8 text-center">
      <p class="text-xl text-green-600 dark:text-green-400">✅ No pending approvals</p>
      <p class="text-sm text-gray-500 mt-2">All command executions are approved</p>
    </div>
  {:else}
    <div class="space-y-4">
      {#each approvals as approval}
        <div class="bg-white dark:bg-gray-800 rounded-lg p-4 shadow border-l-4 {getStatusColor(approval.approved)}">
          <div class="flex items-start justify-between mb-3">
            <div>
              <h3 class="font-semibold">Execution Approval Needed</h3>
              <p class="text-sm text-gray-500">{formatRemaining(approval.expiresAtMs)}</p>
            </div>
            <span class={`px-2 py-1 text-xs rounded-full text-white ${getStatusColor(approval.approved)}`}>
              {approval.approved === null ? 'Pending' : approval.approved ? 'Approved' : 'Denied'}
            </span>
          </div>
          
          <div class="bg-gray-100 dark:bg-gray-900 rounded p-3 mb-3">
            <code class="text-sm break-all">{approval.request?.command || 'N/A'}</code>
          </div>
          
          <div class="grid grid-cols-2 gap-2 text-sm mb-3">
            <div>
              <span class="text-gray-500">Host:</span>
              <span class="ml-2 font-mono">{approval.request?.host || 'local'}</span>
            </div>
            <div>
              <span class="text-gray-500">Requested by:</span>
              <span class="ml-2">{approval.request?.requestedBy || 'Unknown'}</span>
            </div>
          </div>
          
          <div class="flex gap-2">
            <button class="px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700">
              ✅ Approve
            </button>
            <button class="px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700">
              ❌ Deny
            </button>
          </div>
        </div>
      {/each}
    </div>
  {/if}
</div>

<style>
  .exec-approval-panel {
    padding: 1rem;
  }
</style>
